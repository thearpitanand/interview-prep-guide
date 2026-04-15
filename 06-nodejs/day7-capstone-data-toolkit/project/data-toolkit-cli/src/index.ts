// index.ts — CLI entry point. Parse argv, dispatch to command handler.

import { parseArgs } from "./args.ts";
import { runFlatten } from "./commands/flatten.ts";
import { runGroup } from "./commands/group.ts";
import { runJoin } from "./commands/join.ts";
import { runPivot } from "./commands/pivot.ts";
import { runValidate } from "./commands/validate.ts";
import { runTable } from "./commands/table.ts";

function main(): void {
  throw new Error("TODO: implement CLI entry point");
}

main();
