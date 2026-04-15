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
  throw new Error("TODO: implement readNdjson");
  yield undefined as never;
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
  throw new Error("TODO: implement runPipeline");
}
