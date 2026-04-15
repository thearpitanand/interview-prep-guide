// commands/join.ts — Handler for the `join` subcommand.

import { readFile } from "../io/read.ts";
import { writeOutput } from "../io/write.ts";
import { joinRecords, parseJoinKeys } from "../transforms/join.ts";
import type { JoinOptions } from "../args.ts";

export function runJoin(opts: JoinOptions): void {
  // Both files are read as JSON by default; infer individually
  throw new Error("TODO: implement runJoin");
}
