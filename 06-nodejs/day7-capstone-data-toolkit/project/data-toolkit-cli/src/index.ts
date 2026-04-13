// index.ts — CLI entry point. Parse argv, dispatch to command handler.

import { parseArgs } from "./args.ts";
import { runFlatten } from "./commands/flatten.ts";
import { runGroup } from "./commands/group.ts";
import { runJoin } from "./commands/join.ts";
import { runPivot } from "./commands/pivot.ts";
import { runValidate } from "./commands/validate.ts";
import { runTable } from "./commands/table.ts";

function main(): void {
  const opts = parseArgs(process.argv);

  try {
    switch (opts.command) {
      case "flatten":
        runFlatten(opts);
        break;
      case "group":
        runGroup(opts);
        break;
      case "join":
        runJoin(opts);
        break;
      case "pivot":
        runPivot(opts);
        break;
      case "validate":
        runValidate(opts);
        break;
      case "table":
        runTable(opts);
        break;
      default: {
        // TypeScript exhaustiveness check
        const _exhaustive: never = opts;
        throw new Error(`Unhandled command: ${JSON.stringify(_exhaustive)}`);
      }
    }
  } catch (err) {
    // Input errors: show a clean message and exit 1
    if (err instanceof Error) {
      process.stderr.write(`Error: ${err.message}\n`);
    } else {
      process.stderr.write(`Unexpected error: ${String(err)}\n`);
    }
    process.exit(1);
  }
}

main();
