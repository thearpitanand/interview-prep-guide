// flatten.ts — Recursively flatten nested objects into dot-separated keys.

type Row = Record<string, unknown>;

/**
 * Flatten a single nested object into a flat record.
 *
 * Example:
 *   { a: { b: 1 }, c: 2 }  →  { "a.b": 1, c: 2 }
 */
export function flattenRecord(
  obj: Record<string, unknown>,
  prefix = "",
  separator = "."
): Row {
  throw new Error("TODO: implement flattenRecord");
}

/**
 * Flatten an array of potentially nested records.
 */
export function flattenRecords(rows: Row[], separator = "."): Row[] {
  throw new Error("TODO: implement flattenRecords");
}
