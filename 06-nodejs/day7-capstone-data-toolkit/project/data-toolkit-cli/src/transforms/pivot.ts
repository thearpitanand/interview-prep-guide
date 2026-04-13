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
  // Collect unique column values (preserving insertion order)
  const colValues: string[] = [];
  const colValueSet = new Set<string>();

  for (const row of rows) {
    const cv = String(row[colKey] ?? "");
    if (!colValueSet.has(cv)) {
      colValueSet.add(cv);
      colValues.push(cv);
    }
  }

  // Collect unique row key values
  const rowValues: string[] = [];
  const rowValueSet = new Set<string>();
  for (const row of rows) {
    const rv = String(row[rowKey] ?? "");
    if (!rowValueSet.has(rv)) {
      rowValueSet.add(rv);
      rowValues.push(rv);
    }
  }

  // Build lookup: rowValue → colValue → first matching value
  type CellMap = Map<string, unknown>;
  const lookup = new Map<string, CellMap>();

  for (const row of rows) {
    const rv = String(row[rowKey] ?? "");
    const cv = String(row[colKey] ?? "");
    let cellMap = lookup.get(rv);
    if (!cellMap) {
      cellMap = new Map<string, unknown>();
      lookup.set(rv, cellMap);
    }
    // Only take the first matching value
    if (!cellMap.has(cv)) {
      cellMap.set(cv, row[valueKey] ?? null);
    }
  }

  // Assemble output
  return rowValues.map(rv => {
    const cellMap = lookup.get(rv);
    const outputRow: Row = { [rowKey]: rv };
    for (const cv of colValues) {
      outputRow[cv] = cellMap?.get(cv) ?? null;
    }
    return outputRow;
  });
}
