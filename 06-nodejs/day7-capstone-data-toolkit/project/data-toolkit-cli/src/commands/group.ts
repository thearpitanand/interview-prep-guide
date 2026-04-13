// commands/group.ts — Handler for the `group` subcommand.

import { readFile } from "../io/read.ts";
import { writeOutput } from "../io/write.ts";
import { groupBy, parseAggSpec } from "../transforms/group.ts";
import type { GroupOptions } from "../args.ts";

export function runGroup(opts: GroupOptions): void {
  const rows = readFile(opts.file, opts.input);
  const agg = parseAggSpec(opts.agg);
  const result = groupBy(rows, opts.by, agg);
  writeOutput(result, opts.format);
}
