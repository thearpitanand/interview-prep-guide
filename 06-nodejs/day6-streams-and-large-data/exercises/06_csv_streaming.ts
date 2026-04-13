/**
 * Exercise 06 — CSV Streaming with csv-parse & csv-stringify
 *
 * Topics: csv-parse as a Transform stream, columns:true for header-driven
 *         parsing, object mode, csv-stringify for writing, pipeline, numeric
 *         aggregation over a stream.
 *
 * Run: npx tsx 06-nodejs/day6-streams-and-large-data/exercises/06_csv_streaming.ts
 */

import {
  createReadStream,
  createWriteStream,
  writeFileSync,
  readFileSync,
  unlinkSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { pipeline } from "node:stream/promises";
import { Writable, Readable } from "node:stream";
import { parse } from "csv-parse";
import { stringify } from "csv-stringify";
import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

/** Raw row as parsed from CSV — all values are strings by default. */
interface RawSaleRow {
  product: string;
  category: string;
  amount: string;
  quantity: string;
}

/** Transformed row with numeric fields. */
interface SaleRow {
  product: string;
  category: string;
  amount: number;
  quantity: number;
}

interface SummaryRow {
  category: string;
  total_amount: number;
  total_quantity: number;
  row_count: number;
}

// ---------------------------------------------------------------------------
// Streaming helpers
// ---------------------------------------------------------------------------

/**
 * Stream-parse a CSV file and return an async iterable of typed rows.
 * Uses csv-parse with columns:true so headers become object keys.
 */
function streamCsv<T>(path: string): AsyncIterable<T> {
  return createReadStream(path, { encoding: "utf8" }).pipe(
    parse({ columns: true, trim: true, skip_empty_lines: true })
  ) as AsyncIterable<T>;
}

/**
 * Count rows and sum a numeric field in a CSV, fully streamed.
 */
async function aggregateCsv(
  path: string,
  sumField: keyof RawSaleRow
): Promise<{ rowCount: number; sum: number }> {
  let rowCount = 0;
  let sum = 0;

  for await (const row of streamCsv<RawSaleRow>(path)) {
    rowCount++;
    sum += parseFloat(row[sumField] ?? "0");
  }

  return { rowCount, sum };
}

/**
 * Group CSV rows by category, accumulating totals.
 * Memory is bounded: one Map entry per unique category.
 */
async function groupByCategory(path: string): Promise<Map<string, SummaryRow>> {
  const acc = new Map<string, SummaryRow>();

  for await (const raw of streamCsv<RawSaleRow>(path)) {
    const row: SaleRow = {
      product: raw.product,
      category: raw.category,
      amount: parseFloat(raw.amount),
      quantity: parseInt(raw.quantity, 10),
    };

    const existing = acc.get(row.category);
    if (existing) {
      existing.total_amount += row.amount;
      existing.total_quantity += row.quantity;
      existing.row_count++;
    } else {
      acc.set(row.category, {
        category: row.category,
        total_amount: row.amount,
        total_quantity: row.quantity,
        row_count: 1,
      });
    }
  }

  return acc;
}

/**
 * Write an array of objects to a CSV file using csv-stringify + pipeline.
 */
async function writeCsv<T extends Record<string, unknown>>(
  path: string,
  rows: T[],
  header: boolean = true
): Promise<void> {
  await pipeline(
    Readable.from(rows),
    stringify({ header, cast: { number: (v) => v.toString() } }),
    createWriteStream(path)
  );
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
  const tmpCsvIn = join(tmpdir(), `day6_ex06_in_${process.pid}.csv`);
  const tmpCsvOut = join(tmpdir(), `day6_ex06_out_${process.pid}.csv`);

  try {
    // -----------------------------------------------------------------------
    // Set up: create a temp CSV with known data
    // -----------------------------------------------------------------------
    const csvContent = [
      "product,category,amount,quantity",
      "Widget A,electronics,19.99,3",
      "Gadget B,electronics,49.99,1",
      "Book C,books,12.99,5",
      "Book D,books,8.99,2",
      "Pen E,stationery,1.99,10",
    ].join("\n");

    writeFileSync(tmpCsvIn, csvContent, "utf8");

    // -----------------------------------------------------------------------
    // Test 1: row count
    // -----------------------------------------------------------------------
    const { rowCount } = await aggregateCsv(tmpCsvIn, "amount");
    assert.equal(rowCount, 5, `Expected 5 rows, got ${rowCount}`);

    // -----------------------------------------------------------------------
    // Test 2: numeric column sum
    // -----------------------------------------------------------------------
    const { sum: totalAmount } = await aggregateCsv(tmpCsvIn, "amount");
    const expectedTotal = 19.99 + 49.99 + 12.99 + 8.99 + 1.99;
    // Use tolerance for floating point
    assert.ok(
      Math.abs(totalAmount - expectedTotal) < 0.001,
      `Amount sum mismatch: got ${totalAmount}, expected ${expectedTotal}`
    );

    // -----------------------------------------------------------------------
    // Test 3: groupBy produces correct aggregations
    // -----------------------------------------------------------------------
    const summary = await groupByCategory(tmpCsvIn);

    assert.equal(summary.size, 3, `Expected 3 categories, got ${summary.size}`);

    const electronics = summary.get("electronics");
    assert.ok(electronics !== undefined, "electronics category should exist");
    assert.equal(electronics.row_count, 2, "electronics should have 2 rows");
    assert.ok(
      Math.abs(electronics.total_amount - (19.99 + 49.99)) < 0.001,
      "electronics total_amount mismatch"
    );
    assert.equal(electronics.total_quantity, 4, "electronics total_quantity should be 4");

    const books = summary.get("books");
    assert.ok(books !== undefined, "books category should exist");
    assert.equal(books.row_count, 2, "books should have 2 rows");
    assert.equal(books.total_quantity, 7, "books total_quantity should be 7");

    const stationery = summary.get("stationery");
    assert.ok(stationery !== undefined, "stationery category should exist");
    assert.equal(stationery.row_count, 1, "stationery should have 1 row");

    // -----------------------------------------------------------------------
    // Test 4: write summary CSV and read it back
    // -----------------------------------------------------------------------
    const summaryRows = [...summary.values()].sort((a, b) =>
      a.category.localeCompare(b.category)
    );

    await writeCsv(tmpCsvOut, summaryRows);

    const writtenContent = readFileSync(tmpCsvOut, "utf8");
    // csv-stringify writes a header row and then data rows
    assert.ok(writtenContent.includes("category"), "Output CSV should contain 'category' header");
    assert.ok(writtenContent.includes("electronics"), "Output CSV should contain 'electronics'");
    assert.ok(writtenContent.includes("books"), "Output CSV should contain 'books'");

    // -----------------------------------------------------------------------
    // Test 5: round-trip — write then read back with csv-parse
    // -----------------------------------------------------------------------
    const written: Array<{ category: string; total_amount: string; total_quantity: string; row_count: string }> = [];

    await pipeline(
      createReadStream(tmpCsvOut, { encoding: "utf8" }),
      parse({ columns: true, trim: true, skip_empty_lines: true }),
      new Writable({
        objectMode: true,
        write(row, _enc, cb) {
          written.push(row as typeof written[number]);
          cb();
        },
      })
    );

    assert.equal(written.length, 3, `Round-trip should yield 3 rows, got ${written.length}`);

    // Rows are sorted by category alphabetically
    const booksRow = written.find((r) => r.category === "books");
    assert.ok(booksRow !== undefined, "Round-trip: books row should exist");
    assert.equal(
      parseInt(booksRow.row_count, 10),
      2,
      "Round-trip: books row_count should be 2"
    );

    // -----------------------------------------------------------------------
    // Test 6: empty CSV (header only) yields 0 rows
    // -----------------------------------------------------------------------
    writeFileSync(tmpCsvIn, "product,category,amount,quantity\n", "utf8");
    const { rowCount: emptyCount } = await aggregateCsv(tmpCsvIn, "amount");
    assert.equal(emptyCount, 0, "Header-only CSV should yield 0 rows");
  } finally {
    for (const f of [tmpCsvIn, tmpCsvOut]) {
      try { unlinkSync(f); } catch { /* already gone */ }
    }
  }

  console.log("All tests passed!");
}

await main();
