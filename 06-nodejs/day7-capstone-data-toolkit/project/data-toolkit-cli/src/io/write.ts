// write.ts — Format typed arrays and write to stdout.

import { stringify as stringifyCSV } from "csv-stringify/sync";
import { renderTable } from "./table.ts";
import type { Format } from "../args.ts";

type Row = Record<string, unknown>;

/**
 * Format rows according to the desired output format and write to stdout.
 */
export function writeOutput(rows: Row[], format: Format): void {
  const output = formatOutput(rows, format);
  process.stdout.write(output);
}

/**
 * Pure formatter — returns a string. Useful for testing.
 */
export function formatOutput(rows: Row[], format: Format): string {
  switch (format) {
    case "json":
      return JSON.stringify(rows, null, 2) + "\n";

    case "csv": {
      if (rows.length === 0) return "\n";
      return stringifyCSV(rows, { header: true });
    }

    case "table":
      return renderTable(rows);

    default: {
      const _exhaustive: never = format;
      throw new Error(`Unknown format: ${String(_exhaustive)}`);
    }
  }
}
