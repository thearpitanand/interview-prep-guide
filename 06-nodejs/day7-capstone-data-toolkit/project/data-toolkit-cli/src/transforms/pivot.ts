// pivot.ts — Pivot rows into columns.

type Row = Record<string, unknown>;

/**
 * Pivot a flat table by rotating unique values of `colKey` into column headers.
 *
 * Each output row corresponds to a unique value of `rowKey`.
 * Each column (besides `rowKey`) corresponds to a unique value of `colKey`.
 * Cell values are the first matching `valueKey` from the input rows.
 *
 * Example input:
 *   [
 *     { category: "electronics", status: "shipped", amount: 1200 },
 *     { category: "electronics", status: "delivered", amount: 60 },
 *     { category: "furniture",   status: "pending",   amount: 350 },
 *   ]
 *
 * pivot(rows, "category", "status", "amount") →
 *   [
 *     { category: "electronics", shipped: 1200, delivered: 60, pending: null },
 *     { category: "furniture",   shipped: null, delivered: null, pending: 350 },
 *   ]
 */
export function pivot(
  rows: Row[],
  rowKey: string,
  colKey: string,
  valueKey: string
): Row[] {
  throw new Error("TODO: implement pivot");
}
