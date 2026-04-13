// args.ts — stdlib-only argv parser. No external dependencies.

export type Format = "json" | "csv" | "table";
export type InputFormat = "json" | "ndjson" | "csv";
export type JoinType = "inner" | "left";

export interface GlobalOptions {
  format: Format;
  input: InputFormat;
}

export interface FlattenOptions extends GlobalOptions {
  command: "flatten";
  file: string;
}

export interface GroupOptions extends GlobalOptions {
  command: "group";
  file: string;
  by: string;
  agg: string; // e.g. "sum:amount" | "count"
}

export interface JoinOptions extends GlobalOptions {
  command: "join";
  leftFile: string;
  rightFile: string;
  on: string; // e.g. "userId=id"
  type: JoinType;
}

export interface PivotOptions extends GlobalOptions {
  command: "pivot";
  file: string;
  row: string;
  col: string;
  value: string;
}

export interface ValidateOptions extends GlobalOptions {
  command: "validate";
  file: string;
  schema: string;
}

export interface TableOptions extends GlobalOptions {
  command: "table";
  file: string;
}

export type ParsedArgs =
  | FlattenOptions
  | GroupOptions
  | JoinOptions
  | PivotOptions
  | ValidateOptions
  | TableOptions;

// ---- Raw parsing ----

interface RawParsed {
  command: string | undefined;
  positionals: string[];
  flags: Record<string, string | boolean>;
}

function parseRaw(argv: string[]): RawParsed {
  const args = argv.slice(2);
  const command = args[0];
  const positionals: string[] = [];
  const flags: Record<string, string | boolean> = {};

  for (let i = 1; i < args.length; i++) {
    const arg = args[i];
    if (arg === undefined) continue;

    if (arg.startsWith("--")) {
      const key = arg.slice(2);
      const next = args[i + 1];
      if (next !== undefined && !next.startsWith("--")) {
        flags[key] = next;
        i++;
      } else {
        flags[key] = true;
      }
    } else {
      positionals.push(arg);
    }
  }

  return { command, positionals, flags };
}

// ---- Helpers ----

function inferInputFormat(filePath: string): InputFormat {
  if (filePath.endsWith(".ndjson") || filePath.endsWith(".jsonl")) return "ndjson";
  if (filePath.endsWith(".csv")) return "csv";
  return "json";
}

function resolveFormat(flags: Record<string, string | boolean>): Format {
  const f = flags["format"];
  if (f === "json" || f === "csv" || f === "table") return f;
  return "table";
}

function resolveInputFormat(
  flags: Record<string, string | boolean>,
  file: string
): InputFormat {
  const f = flags["input"];
  if (f === "json" || f === "ndjson" || f === "csv") return f;
  return inferInputFormat(file);
}

function resolveJoinType(flags: Record<string, string | boolean>): JoinType {
  const t = flags["type"];
  if (t === "inner" || t === "left") return t;
  return "left";
}

// ---- Public API ----

export function parseArgs(argv: string[]): ParsedArgs {
  const { command, positionals, flags } = parseRaw(argv);

  if (!command) {
    printHelp();
    process.exit(0);
  }

  switch (command) {
    case "flatten": {
      const file = positionals[0];
      if (!file) die("flatten requires a <file> argument");
      return {
        command: "flatten",
        file,
        format: resolveFormat(flags),
        input: resolveInputFormat(flags, file),
      };
    }

    case "group": {
      const file = positionals[0];
      if (!file) die("group requires a <file> argument");
      const by = flags["by"];
      if (typeof by !== "string") die("group requires --by <key>");
      const agg = flags["agg"];
      return {
        command: "group",
        file,
        by,
        agg: typeof agg === "string" ? agg : "count",
        format: resolveFormat(flags),
        input: resolveInputFormat(flags, file),
      };
    }

    case "join": {
      const leftFile = positionals[0];
      const rightFile = positionals[1];
      if (!leftFile || !rightFile) die("join requires <left.json> <right.json>");
      const on = flags["on"];
      if (typeof on !== "string") die("join requires --on <leftKey>=<rightKey>");
      return {
        command: "join",
        leftFile,
        rightFile,
        on,
        type: resolveJoinType(flags),
        format: resolveFormat(flags),
        input: resolveInputFormat(flags, leftFile),
      };
    }

    case "pivot": {
      const file = positionals[0];
      if (!file) die("pivot requires a <file> argument");
      const row = flags["row"];
      const col = flags["col"];
      const value = flags["value"];
      if (typeof row !== "string") die("pivot requires --row <key>");
      if (typeof col !== "string") die("pivot requires --col <key>");
      if (typeof value !== "string") die("pivot requires --value <key>");
      return {
        command: "pivot",
        file,
        row,
        col,
        value,
        format: resolveFormat(flags),
        input: resolveInputFormat(flags, file),
      };
    }

    case "validate": {
      const file = positionals[0];
      if (!file) die("validate requires a <file> argument");
      const schema = flags["schema"];
      if (typeof schema !== "string") die("validate requires --schema <name>");
      return {
        command: "validate",
        file,
        schema,
        format: resolveFormat(flags),
        input: resolveInputFormat(flags, file),
      };
    }

    case "table": {
      const file = positionals[0];
      if (!file) die("table requires a <file> argument");
      return {
        command: "table",
        file,
        format: "table",
        input: resolveInputFormat(flags, file),
      };
    }

    default:
      die(`unknown command "${command}". Run with no arguments to see usage.`);
  }
}

function die(message: string): never {
  process.stderr.write(`Error: ${message}\n`);
  process.exit(1);
}

function printHelp(): void {
  process.stdout.write(`
data-toolkit — read, transform, and export structured data

Usage:
  npx tsx src/index.ts <command> [options]

Commands:
  flatten <file>           Flatten nested JSON records
  group <file>             Group records by a key, with optional aggregation
  join <left> <right>      Join two files on a key
  pivot <file>             Pivot rows into columns
  validate <file>          Validate records against a named Zod schema
  table <file>             Pretty-print a JSON array as an ASCII table

Global Options:
  --format json|csv|table  Output format (default: table)
  --input  json|ndjson|csv Input format (default: infer from extension)

Command Options:
  group:    --by <key> --agg count|sum:<col>
  join:     --on <leftKey>=<rightKey> --type inner|left
  pivot:    --row <key> --col <key> --value <key>
  validate: --schema user|transaction|order

Examples:
  npx tsx src/index.ts flatten fixtures/users.json --format csv
  npx tsx src/index.ts group fixtures/orders.json --by category --agg sum:amount
  npx tsx src/index.ts join fixtures/users.json fixtures/orders.json --on id=userId
  npx tsx src/index.ts pivot fixtures/orders.json --row category --col status --value amount
  npx tsx src/index.ts validate fixtures/users.json --schema user
  npx tsx src/index.ts table fixtures/people.csv
`);
}
