// read.ts — Read JSON, NDJSON, and CSV files into typed arrays.

import { readFileSync } from "node:fs";
import { parse as parseCSV } from "csv-parse/sync";
import type { InputFormat } from "../args.ts";

type Row = Record<string, unknown>;

/**
 * Read a file and parse it into an array of records.
 * Throws on I/O errors or parse failures.
 */
export function readFile(filePath: string, format: InputFormat): Row[] {
  throw new Error("TODO: implement readFile");
}
