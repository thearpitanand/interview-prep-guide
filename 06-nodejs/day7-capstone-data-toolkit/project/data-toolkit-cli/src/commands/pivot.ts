// commands/pivot.ts — Handler for the `pivot` subcommand.

import { readFile } from "../io/read.ts";
import { writeOutput } from "../io/write.ts";
import { pivot } from "../transforms/pivot.ts";
import type { PivotOptions } from "../args.ts";

export function runPivot(opts: PivotOptions): void {
  const rows = readFile(opts.file, opts.input);
  const result = pivot(rows, opts.row, opts.col, opts.value);
  writeOutput(result, opts.format);
}
