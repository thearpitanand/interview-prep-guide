/**
 * Exercise 04 — Pivot Rows to Columns
 *
 * Topics: dynamic column discovery, aggregation, Record<string, number> output
 *
 * Input:  { month, category, amount }[]
 * Output: { month: string } & Record<category, number>
 *         One row per month; each category becomes a column with summed amounts.
 *
 * Missing categories in a row are filled with 0 (not undefined).
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

type SaleRow = {
  month: string;
  category: string;
  amount: number;
};

// A pivot row has a string rowKey plus one numeric column per category
type PivotRow = { month: string } & Record<string, number>;

// ---------------------------------------------------------------------------
// groupBy (local copy — no imports between exercises)
// ---------------------------------------------------------------------------

function groupBy<T>(arr: readonly T[], fn: (item: T) => string): Record<string, T[]> {
  const result: Record<string, T[]> = {};
  for (const item of arr) {
    const key = fn(item);
    if (result[key] === undefined) result[key] = [];
    result[key]!.push(item);
  }
  return result;
}

// ---------------------------------------------------------------------------
// pivot
// ---------------------------------------------------------------------------

/**
 * Transforms a flat table into a pivot table.
 *
 * @param rows      Source rows
 * @param rowKey    The field whose distinct values become pivot row identifiers
 * @param colKey    The field whose distinct values become column headers
 * @param valueKey  The numeric field to aggregate
 * @param agg       Aggregation function (default: sum)
 *
 * Rows in the output follow the order in which `rowKey` values first appear
 * in the input. Sort your input before calling if you need a specific order.
 * All discovered column values appear in every output row (0-filled if absent).
 */
export function pivot(
  rows: readonly SaleRow[],
  rowKey: keyof SaleRow,
  colKey: keyof SaleRow,
  valueKey: keyof SaleRow,
  agg: (acc: number, val: number) => number = (a, b) => a + b
): PivotRow[] {
  if (rows.length === 0) return [];

  // Step 1: discover all column values in input order (deduped)
  const seenCols = new Set<string>();
  const cols: string[] = [];
  for (const row of rows) {
    const colVal = String(row[colKey]);
    if (!seenCols.has(colVal)) {
      seenCols.add(colVal);
      cols.push(colVal);
    }
  }

  // Step 2: group rows by rowKey
  const groups = groupBy(rows, r => String(r[rowKey]));

  // Step 3: preserve rowKey insertion order
  const rowOrder: string[] = [];
  const seenRows = new Set<string>();
  for (const row of rows) {
    const val = String(row[rowKey]);
    if (!seenRows.has(val)) {
      seenRows.add(val);
      rowOrder.push(val);
    }
  }

  // Step 4: build one output row per distinct rowKey value
  return rowOrder.map(rowVal => {
    const groupRows = groups[rowVal] ?? [];

    // Start with zeroes for all columns
    const pivotRow: PivotRow = { month: rowVal };
    for (const col of cols) {
      pivotRow[col] = 0;
    }

    // Aggregate values into the appropriate column
    for (const r of groupRows) {
      const col = String(r[colKey]);
      const val = Number(r[valueKey]);
      pivotRow[col] = agg(pivotRow[col] ?? 0, val);
    }

    return pivotRow;
  });
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  const sales: SaleRow[] = [
    { month: "2024-01", category: "electronics", amount: 299.99 },
    { month: "2024-01", category: "accessories", amount: 49.99  },
    { month: "2024-01", category: "electronics", amount: 599.00 },
    { month: "2024-02", category: "clothing",    amount: 89.99  },
    { month: "2024-02", category: "electronics", amount: 149.00 },
    { month: "2024-02", category: "food",        amount: 12.50  },
    { month: "2024-03", category: "accessories", amount: 29.99  },
    { month: "2024-03", category: "clothing",    amount: 199.00 },
    { month: "2024-03", category: "food",        amount: 34.00  },
  ];

  const result = pivot(sales, "month", "category", "amount");

  // Should produce 3 rows (one per month)
  assert.equal(result.length, 3);

  // All rows should have the same set of column keys
  const expectedCols = new Set(["month", "electronics", "accessories", "clothing", "food"]);
  for (const row of result) {
    assert.deepEqual(new Set(Object.keys(row)), expectedCols);
  }

  // January: electronics = 299.99 + 599.00 = 898.99, accessories = 49.99
  const jan = result.find(r => r.month === "2024-01");
  assert.ok(jan !== undefined, "January row missing");
  assert.ok(Math.abs((jan["electronics"] ?? 0) - 898.99) < 0.001);
  assert.ok(Math.abs((jan["accessories"] ?? 0) - 49.99)  < 0.001);
  assert.equal(jan["clothing"], 0);
  assert.equal(jan["food"],     0);

  // February: clothing = 89.99, electronics = 149.00, food = 12.50
  const feb = result.find(r => r.month === "2024-02");
  assert.ok(feb !== undefined, "February row missing");
  assert.ok(Math.abs((feb["clothing"]    ?? 0) - 89.99)  < 0.001);
  assert.ok(Math.abs((feb["electronics"] ?? 0) - 149.00) < 0.001);
  assert.ok(Math.abs((feb["food"]        ?? 0) - 12.50)  < 0.001);
  assert.equal(feb["accessories"], 0);

  // March: accessories = 29.99, clothing = 199.00, food = 34.00
  const mar = result.find(r => r.month === "2024-03");
  assert.ok(mar !== undefined, "March row missing");
  assert.ok(Math.abs((mar["accessories"] ?? 0) - 29.99)  < 0.001);
  assert.ok(Math.abs((mar["clothing"]    ?? 0) - 199.00) < 0.001);
  assert.ok(Math.abs((mar["food"]        ?? 0) - 34.00)  < 0.001);
  assert.equal(mar["electronics"], 0);

  // --- Row order mirrors input order ---
  assert.equal(result[0]?.month, "2024-01");
  assert.equal(result[1]?.month, "2024-02");
  assert.equal(result[2]?.month, "2024-03");

  // --- Custom aggregation: count instead of sum ---
  const counted = pivot(sales, "month", "category", "amount", (acc, _) => acc + 1);
  const janCount = counted.find(r => r.month === "2024-01");
  assert.ok(janCount !== undefined);
  assert.equal(janCount["electronics"], 2); // two electronics rows in Jan
  assert.equal(janCount["accessories"], 1);

  // --- Empty input ---
  assert.deepEqual(pivot([], "month", "category", "amount"), []);

  // --- Single row ---
  const single = pivot(
    [{ month: "2024-06", category: "food", amount: 9.99 }],
    "month", "category", "amount"
  );
  assert.equal(single.length, 1);
  assert.ok(Math.abs((single[0]?.["food"] ?? 0) - 9.99) < 0.001);

  console.log("All tests passed!");
}
