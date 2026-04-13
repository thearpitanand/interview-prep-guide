/**
 * pipeline.ts — The streaming ETL pipeline.
 *
 * Flow:
 *   readNdjson (async generator)
 *     → validate with Zod (drop invalid, count errors)
 *     → update in-memory aggregator Map (bounded by 20 categories)
 *     → (on completion) emit summary rows
 *     → write CSV via csv-stringify + fs.createWriteStream
 *
 * Memory: bounded. The input file is never held in memory.
 * The aggregator Map holds at most 20 entries regardless of row count.
 */

import { createReadStream, createWriteStream } from "node:fs";
import { createInterface } from "node:readline";
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";
import { stringify } from "csv-stringify";
import {
  EventRecordSchema,
  type EventRecord,
  type CategorySummary,
  type Category,
} from "./schema.js";

// ---------------------------------------------------------------------------
// readNdjson — async generator, streams one record at a time
// ---------------------------------------------------------------------------

/**
 * Stream-parse an NDJSON file, yielding one typed value per line.
 * Skips blank lines. Calls onMalformed for bad JSON without crashing.
 */
async function* readNdjson<T>(
  path: string,
  onMalformed?: (line: string, err: unknown) => void
): AsyncGenerator<T> {
  const fileStream = createReadStream(path, { encoding: "utf8" });
  const rl = createInterface({ input: fileStream, crlfDelay: Infinity });

  for await (const line of rl) {
    const trimmed = line.trim();
    if (!trimmed) continue;
    try {
      yield JSON.parse(trimmed) as T;
    } catch (err) {
      onMalformed?.(trimmed, err);
    }
  }
}

// ---------------------------------------------------------------------------
// Aggregator
// ---------------------------------------------------------------------------

function makeAggregator(): Map<Category, CategorySummary> {
  return new Map<Category, CategorySummary>();
}

function updateAggregator(
  acc: Map<Category, CategorySummary>,
  record: EventRecord
): void {
  const existing = acc.get(record.category);
  if (existing) {
    existing.event_count++;
    existing.total_amount_cents += record.amountCents;
    existing.total_quantity += record.quantity;
    if (record.flagged) existing.flagged_count++;
  } else {
    acc.set(record.category, {
      category: record.category,
      event_count: 1,
      total_amount_cents: record.amountCents,
      total_quantity: record.quantity,
      flagged_count: record.flagged ? 1 : 0,
      avg_amount_cents: 0, // computed at flush
    });
  }
}

function finalizeAggregator(acc: Map<Category, CategorySummary>): CategorySummary[] {
  const rows: CategorySummary[] = [];
  for (const row of acc.values()) {
    rows.push({
      ...row,
      avg_amount_cents:
        row.event_count > 0
          ? Math.round(row.total_amount_cents / row.event_count)
          : 0,
    });
  }
  return rows.sort((a, b) => a.category.localeCompare(b.category));
}

// ---------------------------------------------------------------------------
// Pipeline result
// ---------------------------------------------------------------------------

export interface PipelineResult {
  rowsRead: number;
  rowsValid: number;
  rowsInvalid: number;
  rowsMalformedJson: number;
  categoriesFound: number;
  summary: CategorySummary[];
  elapsedMs: number;
}

// ---------------------------------------------------------------------------
// runPipeline — the main entry point for the ETL
// ---------------------------------------------------------------------------

export async function runPipeline(
  inputPath: string,
  outputPath: string,
  onProgress?: (rowsRead: number) => void
): Promise<PipelineResult> {
  const start = Date.now();

  let rowsRead = 0;
  let rowsValid = 0;
  let rowsInvalid = 0;
  let rowsMalformedJson = 0;

  const acc = makeAggregator();

  // Phase 1: stream-parse + validate + aggregate
  for await (const raw of readNdjson<unknown>(
    inputPath,
    () => { rowsMalformedJson++; }
  )) {
    rowsRead++;

    const parsed = EventRecordSchema.safeParse(raw);
    if (!parsed.success) {
      rowsInvalid++;
      continue;
    }

    updateAggregator(acc, parsed.data);
    rowsValid++;

    // Report progress every 10,000 rows
    if (onProgress && rowsRead % 10_000 === 0) {
      onProgress(rowsRead);
    }
  }

  // Phase 2: finalize aggregation and write CSV
  const summary = finalizeAggregator(acc);

  await pipeline(
    Readable.from(summary as Record<string, unknown>[]),
    stringify({
      header: true,
      cast: { number: (v) => v.toString() },
    }),
    createWriteStream(outputPath)
  );

  return {
    rowsRead,
    rowsValid,
    rowsInvalid,
    rowsMalformedJson,
    categoriesFound: acc.size,
    summary,
    elapsedMs: Date.now() - start,
  };
}
