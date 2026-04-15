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
  throw new Error("TODO: implement parseAggSpec");
}

/**
 * Group an array of records by a key, applying the given aggregation.
 * Returns one row per unique key value.
 */
export function groupBy(rows: Row[], key: string, agg: AggSpec): Row[] {
  throw new Error("TODO: implement groupBy");
}
