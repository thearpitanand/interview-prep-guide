// group.ts — GroupBy with aggregation (count or sum:<col>).

type Row = Record<string, unknown>;

export type AggSpec =
  | { type: "count" }
  | { type: "sum"; col: string };

/**
 * Parse an aggregation spec string.
 * Accepts: "count" | "sum:<col>"
 */
export function parseAggSpec(spec: string): AggSpec {
  if (spec === "count") return { type: "count" };
  if (spec.startsWith("sum:")) {
    const col = spec.slice(4);
    if (!col) throw new Error(`sum aggregation requires a column name: "${spec}"`);
    return { type: "sum", col };
  }
  throw new Error(`Unknown aggregation spec: "${spec}". Use "count" or "sum:<col>".`);
}

/**
 * Group an array of records by a key, applying the given aggregation.
 * Returns one row per unique key value.
 */
export function groupBy(rows: Row[], key: string, agg: AggSpec): Row[] {
  const groups = new Map<string, Row[]>();

  for (const row of rows) {
    const groupKey = String(row[key] ?? "__undefined__");
    const existing = groups.get(groupKey);
    if (existing) {
      existing.push(row);
    } else {
      groups.set(groupKey, [row]);
    }
  }

  const result: Row[] = [];

  for (const [groupKey, groupRows] of groups) {
    const baseRow: Row = { [key]: groupKey };

    if (agg.type === "count") {
      baseRow["count"] = groupRows.length;
    } else {
      // sum:<col>
      const sum = groupRows.reduce((acc, r) => {
        const v = r[agg.col];
        return acc + (typeof v === "number" ? v : parseFloat(String(v ?? "0")) || 0);
      }, 0);
      baseRow[`sum_${agg.col}`] = Math.round(sum * 100) / 100;
    }

    result.push(baseRow);
  }

  return result;
}
