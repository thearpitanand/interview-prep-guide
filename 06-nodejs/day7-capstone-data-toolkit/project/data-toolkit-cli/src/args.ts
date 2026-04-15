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
  throw new Error("TODO: implement parseRaw");
}

// ---- Helpers ----

function inferInputFormat(filePath: string): InputFormat {
  throw new Error("TODO: implement inferInputFormat");
}

function resolveFormat(flags: Record<string, string | boolean>): Format {
  throw new Error("TODO: implement resolveFormat");
}

function resolveInputFormat(
  flags: Record<string, string | boolean>,
  file: string
): InputFormat {
  throw new Error("TODO: implement resolveInputFormat");
}

function resolveJoinType(flags: Record<string, string | boolean>): JoinType {
  throw new Error("TODO: implement resolveJoinType");
}

// ---- Public API ----

export function parseArgs(argv: string[]): ParsedArgs {
  throw new Error("TODO: implement parseArgs");
}

function die(message: string): never {
  throw new Error("TODO: implement die");
}

function printHelp(): void {
  throw new Error("TODO: implement printHelp");
}
