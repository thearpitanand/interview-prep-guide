// write.ts — Format typed arrays and write to stdout.

import { stringify as stringifyCSV } from "csv-stringify/sync";
import { renderTable } from "./table.ts";
import type { Format } from "../args.ts";

type Row = Record<string, unknown>;

/**
 * Format rows according to the desired output format and write to stdout.
 */
export function writeOutput(rows: Row[], format: Format): void {
  throw new Error("TODO: implement writeOutput");
}

/**
 * Pure formatter — returns a string. Useful for testing.
 */
export function formatOutput(rows: Row[], format: Format): string {
  throw new Error("TODO: implement formatOutput");
}
