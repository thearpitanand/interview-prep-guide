/**
 * Exercise 03 — groupBy, countBy, and indexBy
 *
 * Topics: typed partitioning helpers, Record vs array, O(n) algorithms
 *
 * Three subtly different helpers:
 *   - groupBy  → Record<K, T[]>       all items sharing a key
 *   - countBy  → Record<K, number>    frequency per key
 *   - indexBy  → Record<K, T>         last item per key (assumes unique keys)
 *
 * Tested on a realistic transactions dataset.
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

type Transaction = {
  id: string;
  customerId: string;
  category: "electronics" | "accessories" | "clothing" | "food";
  amount: number;
  month: string; // "2024-01"
};

// ---------------------------------------------------------------------------
// 1. groupBy — partition into arrays
// ---------------------------------------------------------------------------

export function groupBy<T, K extends string>(
  arr: readonly T[],
  fn: (item: T) => K
): Record<K, T[]> {
  const result = {} as Record<K, T[]>;
  for (const item of arr) {
    const key = fn(item);
    if (result[key] === undefined) {
      result[key] = [];
    }
    // Non-null assertion: we just ensured it exists above
    result[key]!.push(item);
  }
  return result;
}

// ---------------------------------------------------------------------------
// 2. countBy — frequency distribution
// ---------------------------------------------------------------------------

export function countBy<T, K extends string>(
  arr: readonly T[],
  fn: (item: T) => K
): Record<K, number> {
  const result = {} as Record<K, number>;
  for (const item of arr) {
    const key = fn(item);
    result[key] = (result[key] ?? 0) + 1;
  }
  return result;
}

// ---------------------------------------------------------------------------
// 3. indexBy — build a lookup table (last value wins on duplicate keys)
// ---------------------------------------------------------------------------

export function indexBy<T, K extends string>(
  arr: readonly T[],
  fn: (item: T) => K
): Record<K, T> {
  const result = {} as Record<K, T>;
  for (const item of arr) {
    result[fn(item)] = item;
  }
  return result;
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  const transactions: Transaction[] = [
    { id: "T01", customerId: "C1", category: "electronics", amount: 299.99, month: "2024-01" },
    { id: "T02", customerId: "C2", category: "accessories", amount: 49.99,  month: "2024-01" },
    { id: "T03", customerId: "C1", category: "clothing",    amount: 89.99,  month: "2024-02" },
    { id: "T04", customerId: "C3", category: "electronics", amount: 599.00, month: "2024-01" },
    { id: "T05", customerId: "C2", category: "food",        amount: 12.50,  month: "2024-02" },
    { id: "T06", customerId: "C1", category: "electronics", amount: 149.00, month: "2024-02" },
    { id: "T07", customerId: "C3", category: "accessories", amount: 29.99,  month: "2024-03" },
    { id: "T08", customerId: "C2", category: "clothing",    amount: 199.00, month: "2024-03" },
  ];

  // ---- groupBy ----

  const byCustomer = groupBy(transactions, t => t.customerId);
  assert.equal(Object.keys(byCustomer).length, 3);
  assert.equal(byCustomer["C1"]?.length, 3); // T01, T03, T06
  assert.equal(byCustomer["C2"]?.length, 3); // T02, T05, T08
  assert.equal(byCustomer["C3"]?.length, 2); // T04, T07

  const byCategory = groupBy(transactions, t => t.category);
  assert.equal(byCategory["electronics"]?.length, 3);
  assert.equal(byCategory["accessories"]?.length, 2);
  assert.equal(byCategory["clothing"]?.length, 2);
  assert.equal(byCategory["food"]?.length, 1);

  const byMonth = groupBy(transactions, t => t.month);
  assert.equal(byMonth["2024-01"]?.length, 3);
  assert.equal(byMonth["2024-02"]?.length, 3);
  assert.equal(byMonth["2024-03"]?.length, 2);

  // ---- countBy ----

  const countByCategory = countBy(transactions, t => t.category);
  assert.equal(countByCategory["electronics"], 3);
  assert.equal(countByCategory["accessories"], 2);
  assert.equal(countByCategory["clothing"],    2);
  assert.equal(countByCategory["food"],        1);

  const countByMonth = countBy(transactions, t => t.month);
  assert.equal(countByMonth["2024-01"], 3);
  assert.equal(countByMonth["2024-02"], 3);
  assert.equal(countByMonth["2024-03"], 2);

  // countBy is consistent with groupBy lengths
  for (const [key, count] of Object.entries(countByCategory)) {
    assert.equal(count, byCategory[key as Transaction["category"]]?.length);
  }

  // ---- indexBy ----

  const byId = indexBy(transactions, t => t.id);
  assert.equal(byId["T01"]?.customerId, "C1");
  assert.equal(byId["T04"]?.amount,     599.00);
  assert.equal(byId["T08"]?.category,   "clothing");
  // Every transaction is reachable by id
  assert.equal(Object.keys(byId).length, transactions.length);

  // ---- edge cases ----

  // Empty array
  const emptyGrouped = groupBy([] as Transaction[], t => t.customerId);
  assert.equal(Object.keys(emptyGrouped).length, 0);

  const emptyCounted = countBy([] as Transaction[], t => t.category);
  assert.equal(Object.keys(emptyCounted).length, 0);

  const emptyIndexed = indexBy([] as Transaction[], t => t.id);
  assert.equal(Object.keys(emptyIndexed).length, 0);

  // Single-item array
  const single = [transactions[0]!];
  assert.equal(groupBy(single, t => t.customerId)["C1"]?.length, 1);
  assert.equal(countBy(single, t => t.category)["electronics"], 1);
  assert.equal(indexBy(single, t => t.id)["T01"]?.amount, 299.99);

  // groupBy result can be used to compute per-group sums
  const totalByCustomer = Object.entries(byCustomer).map(([customerId, txns]) => ({
    customerId,
    total: txns.reduce((sum, t) => sum + t.amount, 0),
  }));
  const c1Total = totalByCustomer.find(r => r.customerId === "C1")?.total ?? 0;
  // T01(299.99) + T03(89.99) + T06(149.00) = 538.98
  assert.ok(Math.abs(c1Total - 538.98) < 0.001);

  console.log("All tests passed!");
}
