// commands/flatten.ts — Handler for the `flatten` subcommand.

import { readFile } from "../io/read.ts";
import { writeOutput } from "../io/write.ts";
import { flattenRecords } from "../transforms/flatten.ts";
import type { FlattenOptions } from "../args.ts";

export function runFlatten(opts: FlattenOptions): void {
  throw new Error("TODO: implement runFlatten");
}
