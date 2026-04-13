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
  const result: Row = {};

  for (const [key, value] of Object.entries(obj)) {
    const fullKey = prefix ? `${prefix}${separator}${key}` : key;

    if (
      typeof value === "object" &&
      value !== null &&
      !Array.isArray(value)
    ) {
      const nested = flattenRecord(value as Record<string, unknown>, fullKey, separator);
      Object.assign(result, nested);
    } else {
      result[fullKey] = value;
    }
  }

  return result;
}

/**
 * Flatten an array of potentially nested records.
 */
export function flattenRecords(rows: Row[], separator = "."): Row[] {
  return rows.map(row => flattenRecord(row, "", separator));
}
