// transforms.test.ts — Unit tests for all pure transform functions.
// Run: npx tsx --test tests/transforms.test.ts

import { describe, it } from "node:test";
import assert from "node:assert/strict";

import { flattenRecord, flattenRecords } from "../src/transforms/flatten.ts";
import { groupBy, parseAggSpec } from "../src/transforms/group.ts";
import { joinRecords, parseJoinKeys } from "../src/transforms/join.ts";
import { pivot } from "../src/transforms/pivot.ts";

// ---- flatten ----

describe("flattenRecord", () => {
  it("returns flat records unchanged", () => {
    const input = { a: 1, b: "hello", c: true };
    assert.deepEqual(flattenRecord(input), { a: 1, b: "hello", c: true });
  });

  it("flattens one level of nesting", () => {
    const input = { name: "Alice", address: { city: "NY", country: "US" } };
    assert.deepEqual(flattenRecord(input), {
      name: "Alice",
      "address.city": "NY",
      "address.country": "US",
    });
  });

  it("flattens two levels of nesting", () => {
    const input = { a: { b: { c: 42 } }, d: 1 };
    assert.deepEqual(flattenRecord(input), { "a.b.c": 42, d: 1 });
  });

  it("preserves arrays as values (does not expand them)", () => {
    const input = { tags: ["x", "y"], name: "test" };
    const result = flattenRecord(input);
    assert.deepEqual(result["tags"], ["x", "y"]);
    assert.equal(result["name"], "test");
  });

  it("uses custom separator", () => {
    const input = { a: { b: 1 } };
    assert.deepEqual(flattenRecord(input, "", "_"), { a_b: 1 });
  });
});

describe("flattenRecords", () => {
  it("flattens an array of records", () => {
    const rows = [
      { id: 1, meta: { score: 100 } },
      { id: 2, meta: { score: 200 } },
    ];
    const result = flattenRecords(rows);
    assert.equal(result.length, 2);
    assert.equal(result[0]?.["meta.score"], 100);
    assert.equal(result[1]?.["meta.score"], 200);
  });

  it("handles an empty array", () => {
    assert.deepEqual(flattenRecords([]), []);
  });
});

// ---- groupBy ----

describe("parseAggSpec", () => {
  it("parses count", () => {
    assert.deepEqual(parseAggSpec("count"), { type: "count" });
  });

  it("parses sum:<col>", () => {
    assert.deepEqual(parseAggSpec("sum:amount"), { type: "sum", col: "amount" });
  });

  it("throws on unknown spec", () => {
    assert.throws(() => parseAggSpec("avg:amount"), /Unknown aggregation spec/);
  });

  it("throws on sum without column", () => {
    assert.throws(() => parseAggSpec("sum:"), /requires a column name/);
  });
});

describe("groupBy", () => {
  const rows = [
    { category: "A", amount: 10 },
    { category: "B", amount: 20 },
    { category: "A", amount: 30 },
    { category: "B", amount: 40 },
    { category: "C", amount: 5 },
  ];

  it("groups and counts", () => {
    const result = groupBy(rows, "category", { type: "count" });
    const byCategory = Object.fromEntries(result.map(r => [r["category"], r["count"]]));
    assert.equal(byCategory["A"], 2);
    assert.equal(byCategory["B"], 2);
    assert.equal(byCategory["C"], 1);
  });

  it("groups and sums", () => {
    const result = groupBy(rows, "category", { type: "sum", col: "amount" });
    const byCategory = Object.fromEntries(result.map(r => [r["category"], r["sum_amount"]]));
    assert.equal(byCategory["A"], 40);
    assert.equal(byCategory["B"], 60);
    assert.equal(byCategory["C"], 5);
  });

  it("returns one row per unique key", () => {
    const result = groupBy(rows, "category", { type: "count" });
    assert.equal(result.length, 3);
  });

  it("handles empty array", () => {
    const result = groupBy([], "category", { type: "count" });
    assert.deepEqual(result, []);
  });

  it("handles missing key values", () => {
    const data = [{ name: "Alice" }, { name: "Bob", category: "X" }];
    const result = groupBy(data, "category", { type: "count" });
    // "undefined" key and "X" key
    assert.equal(result.length, 2);
  });
});

// ---- join ----

describe("parseJoinKeys", () => {
  it("parses leftKey=rightKey", () => {
    assert.deepEqual(parseJoinKeys("userId=id"), { leftKey: "userId", rightKey: "id" });
  });

  it("throws on missing =", () => {
    assert.throws(() => parseJoinKeys("userId"), /must be in the form/);
  });

  it("throws on empty sides", () => {
    assert.throws(() => parseJoinKeys("=id"), /Invalid join keys/);
  });
});

describe("joinRecords", () => {
  const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 3, name: "Carol" },
  ];
  const orders = [
    { orderId: "O1", userId: 1, product: "Laptop" },
    { orderId: "O2", userId: 2, product: "Book" },
    { orderId: "O3", userId: 1, product: "Mouse" },
  ];

  it("inner join — only matched rows", () => {
    const result = joinRecords(users, orders, "id", "userId", "inner");
    // Carol (id=3) has no orders — should be excluded
    assert.equal(result.length, 3); // Alice×2, Bob×1
    const names = result.map(r => r["name"]);
    assert.ok(!names.includes("Carol"));
  });

  it("left join — all left rows, nulls for unmatched", () => {
    const result = joinRecords(users, orders, "id", "userId", "left");
    // Carol should appear even without an order
    assert.equal(result.length, 4); // Alice×2, Bob×1, Carol×1
    const carolRow = result.find(r => r["name"] === "Carol");
    assert.ok(carolRow !== undefined);
    assert.equal(carolRow["orderId"], undefined);
  });

  it("left join is the default", () => {
    const result = joinRecords(users, orders, "id", "userId");
    assert.equal(result.length, 4);
  });

  it("handles empty left array", () => {
    assert.deepEqual(joinRecords([], orders, "id", "userId", "inner"), []);
  });

  it("handles empty right array", () => {
    const result = joinRecords(users, [], "id", "userId", "left");
    // All left rows preserved with no right data
    assert.equal(result.length, 3);
  });

  it("inner join with empty right returns empty", () => {
    const result = joinRecords(users, [], "id", "userId", "inner");
    assert.deepEqual(result, []);
  });
});

// ---- pivot ----

describe("pivot", () => {
  const rows = [
    { category: "electronics", status: "shipped", amount: 1200 },
    { category: "electronics", status: "delivered", amount: 60 },
    { category: "furniture", status: "pending", amount: 350 },
    { category: "education", status: "delivered", amount: 45 },
    { category: "education", status: "delivered", amount: 25 }, // duplicate — first wins
  ];

  it("pivots rows into columns", () => {
    const result = pivot(rows, "category", "status", "amount");
    assert.equal(result.length, 3);

    const electronics = result.find(r => r["category"] === "electronics");
    assert.ok(electronics !== undefined);
    assert.equal(electronics["shipped"], 1200);
    assert.equal(electronics["delivered"], 60);
    assert.equal(electronics["pending"], null);
  });

  it("fills missing cells with null", () => {
    const result = pivot(rows, "category", "status", "amount");
    const furniture = result.find(r => r["category"] === "furniture");
    assert.ok(furniture !== undefined);
    assert.equal(furniture["shipped"], null);
    assert.equal(furniture["delivered"], null);
    assert.equal(furniture["pending"], 350);
  });

  it("first matching value wins for duplicates", () => {
    const result = pivot(rows, "category", "status", "amount");
    const education = result.find(r => r["category"] === "education");
    assert.ok(education !== undefined);
    // First "delivered" row has amount 45
    assert.equal(education["delivered"], 45);
  });

  it("handles empty input", () => {
    assert.deepEqual(pivot([], "row", "col", "val"), []);
  });

  it("preserves insertion order of column values", () => {
    const result = pivot(rows, "category", "status", "amount");
    const firstRow = result[0];
    assert.ok(firstRow !== undefined);
    const keys = Object.keys(firstRow).slice(1); // skip rowKey
    assert.deepEqual(keys, ["shipped", "delivered", "pending"]);
  });
});
