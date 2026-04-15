// commands/group.ts — Handler for the `group` subcommand.

import { readFile } from "../io/read.ts";
import { writeOutput } from "../io/write.ts";
import { groupBy, parseAggSpec } from "../transforms/group.ts";
import type { GroupOptions } from "../args.ts";

export function runGroup(opts: GroupOptions): void {
  throw new Error("TODO: implement runGroup");
}
