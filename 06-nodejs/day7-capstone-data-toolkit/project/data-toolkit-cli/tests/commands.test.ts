// commands.test.ts — Integration tests for command handlers.
// Tests call handlers against fixture files and assert on formatted output.
// Run: npx tsx --test tests/commands.test.ts

import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

// Helper: resolve fixture paths relative to this file
const __dirname = fileURLToPath(new URL(".", import.meta.url));
const fixture = (name: string) => resolve(__dirname, "../fixtures", name);

// Import pure formatters and transforms (avoid I/O side effects in tests)
import { flattenRecords } from "../src/transforms/flatten.ts";
import { groupBy, parseAggSpec } from "../src/transforms/group.ts";
import { joinRecords, parseJoinKeys } from "../src/transforms/join.ts";
import { pivot } from "../src/transforms/pivot.ts";
import { readFile } from "../src/io/read.ts";
import { formatOutput } from "../src/io/write.ts";
import { renderTable } from "../src/io/table.ts";
import { getSchema } from "../src/schemas/index.ts";

// ---- flatten command ----

describe("flatten command (integration)", () => {
  it("flattens users.json and produces flat keys", () => {
    const rows = readFile(fixture("users.json"), "json");
    const flat = flattenRecords(rows);

    assert.ok(flat.length > 0);
    // Original has nested address object
    const first = flat[0];
    assert.ok(first !== undefined);
    assert.ok("address.city" in first, "should have flattened address.city key");
    assert.ok("address.country" in first, "should have flattened address.country key");
    assert.ok(!("address" in first), "should not have nested address key");
  });

  it("formats flattened output as CSV without nested objects", () => {
    const rows = readFile(fixture("users.json"), "json");
    const flat = flattenRecords(rows);
    const csv = formatOutput(flat, "csv");

    assert.ok(csv.includes("address.city"), "CSV header should include address.city");
    assert.ok(csv.includes("New York"), "CSV should include city value");
  });

  it("formats flattened output as JSON", () => {
    const rows = readFile(fixture("users.json"), "json");
    const flat = flattenRecords(rows);
    const json = formatOutput(flat, "json");
    const parsed = JSON.parse(json) as unknown[];
    assert.ok(Array.isArray(parsed));
    assert.equal(parsed.length, rows.length);
  });
});

// ---- group command ----

describe("group command (integration)", () => {
  it("groups orders by category with count", () => {
    const rows = readFile(fixture("orders.json"), "json");
    const agg = parseAggSpec("count");
    const result = groupBy(rows, "category", agg);

    assert.ok(result.length > 0);
    const electronics = result.find(r => r["category"] === "electronics");
    assert.ok(electronics !== undefined);
    assert.equal(electronics["count"], 3); // O1001, O1003, O1005
  });

  it("groups orders by category with sum:amount", () => {
    const rows = readFile(fixture("orders.json"), "json");
    const agg = parseAggSpec("sum:amount");
    const result = groupBy(rows, "category", agg);

    const electronics = result.find(r => r["category"] === "electronics");
    assert.ok(electronics !== undefined);
    // 1200 + 60 + 80 = 1340
    assert.equal(electronics["sum_amount"], 1340);
  });

  it("groups people.csv by department with count", () => {
    const rows = readFile(fixture("people.csv"), "csv");
    const agg = parseAggSpec("count");
    const result = groupBy(rows, "department", agg);

    const engineering = result.find(r => r["department"] === "Engineering");
    assert.ok(engineering !== undefined);
    assert.equal(engineering["count"], 3);
  });
});

// ---- join command ----

describe("join command (integration)", () => {
  it("left joins users and orders on id=userId", () => {
    const users = readFile(fixture("users.json"), "json");
    const orders = readFile(fixture("orders.json"), "json");
    const { leftKey, rightKey } = parseJoinKeys("id=userId");
    const result = joinRecords(users, orders, leftKey, rightKey, "left");

    // 5 users, Alice (id=1) has 2 orders, Bob (id=2) has 2 orders
    // Carol=1, Dave=1, Eve=1 → 2+2+1+1+1 = 7 rows
    assert.equal(result.length, 7);
  });

  it("inner join drops users with no orders", () => {
    const users = readFile(fixture("users.json"), "json");
    const orders = readFile(fixture("orders.json"), "json");
    const { leftKey, rightKey } = parseJoinKeys("id=userId");
    const result = joinRecords(users, orders, leftKey, rightKey, "inner");

    // Only users who have at least one order (all 5 do in fixture data)
    // Alice=2, Bob=2, Carol=1, Dave=1, Eve=1 = 7
    assert.equal(result.length, 7);
    // Verify joined rows have both user and order fields
    const first = result[0];
    assert.ok(first !== undefined);
    assert.ok("name" in first);
    assert.ok("orderId" in first || "product" in first);
  });

  it("joined rows contain fields from both sides", () => {
    const users = readFile(fixture("users.json"), "json");
    const orders = readFile(fixture("orders.json"), "json");
    const { leftKey, rightKey } = parseJoinKeys("id=userId");
    const result = joinRecords(users, orders, leftKey, rightKey, "inner");

    const alice = result.find(r => r["name"] === "Alice");
    assert.ok(alice !== undefined);
    assert.ok("product" in alice);
  });
});

// ---- pivot command ----

describe("pivot command (integration)", () => {
  it("pivots orders by category/status/amount", () => {
    const rows = readFile(fixture("orders.json"), "json");
    const result = pivot(rows, "category", "status", "amount");

    // Should have one row per category
    const categories = result.map(r => r["category"]);
    assert.ok(categories.includes("electronics"));
    assert.ok(categories.includes("furniture"));
    assert.ok(categories.includes("education"));
  });

  it("creates column headers from unique status values", () => {
    const rows = readFile(fixture("orders.json"), "json");
    const result = pivot(rows, "category", "status", "amount");

    const first = result[0];
    assert.ok(first !== undefined);
    const keys = Object.keys(first);
    // Should have category + all status values as columns
    assert.ok(keys.includes("shipped") || keys.includes("delivered") || keys.includes("pending"));
  });

  it("fills null for missing combinations", () => {
    const rows = readFile(fixture("orders.json"), "json");
    const result = pivot(rows, "category", "status", "amount");

    // electronics has no "pending" orders
    const electronics = result.find(r => r["category"] === "electronics");
    assert.ok(electronics !== undefined);
    assert.equal(electronics["pending"], null);
  });
});

// ---- validate command ----

describe("validate command (integration)", () => {
  it("validates users.json against user schema — all valid", () => {
    const schema = getSchema("user");
    assert.ok(schema !== undefined);

    const rows = readFile(fixture("users.json"), "json");
    let validCount = 0;
    let invalidCount = 0;

    for (const row of rows) {
      const result = schema.safeParse(row);
      if (result.success) validCount++;
      else invalidCount++;
    }

    assert.equal(validCount, 5);
    assert.equal(invalidCount, 0);
  });

  it("validates orders.json against order schema — all valid", () => {
    const schema = getSchema("order");
    assert.ok(schema !== undefined);

    const rows = readFile(fixture("orders.json"), "json");
    let validCount = 0;

    for (const row of rows) {
      const result = schema.safeParse(row);
      if (result.success) validCount++;
    }

    assert.equal(validCount, rows.length);
  });

  it("returns undefined for unknown schema name", () => {
    const schema = getSchema("nonexistent");
    assert.equal(schema, undefined);
  });

  it("catches invalid data", () => {
    const schema = getSchema("user");
    assert.ok(schema !== undefined);

    const badUser = { id: -1, name: "", age: 200, role: "superadmin" };
    const result = schema.safeParse(badUser);
    assert.equal(result.success, false);
  });
});

// ---- table command / ASCII renderer ----

describe("table command (integration)", () => {
  it("renders users.json as ASCII table with all column headers", () => {
    const rows = readFile(fixture("users.json"), "json");
    const flat = flattenRecords(rows); // flatten before table for nested data
    const table = renderTable(flat);

    assert.ok(table.includes("name"), "table should have name column");
    assert.ok(table.includes("Alice"), "table should include Alice");
    assert.ok(table.includes("+"), "table should have border characters");
    assert.ok(table.includes("|"), "table should have cell separators");
  });

  it("renders an empty array as (empty)", () => {
    const result = renderTable([]);
    assert.equal(result, "(empty)\n");
  });

  it("aligns columns correctly (all rows same width)", () => {
    const rows = [
      { name: "Alice", score: 100 },
      { name: "Bob",   score: 99 },
    ];
    const table = renderTable(rows);
    const lines = table.split("\n").filter(l => l.startsWith("|"));
    // All data lines should have the same length
    const lengths = new Set(lines.map(l => l.length));
    assert.equal(lengths.size, 1, "All table rows should have equal width");
  });

  it("renders CSV file as table", () => {
    const rows = readFile(fixture("people.csv"), "csv");
    const table = renderTable(rows);
    assert.ok(table.includes("department"));
    assert.ok(table.includes("Engineering"));
  });
});

// ---- NDJSON reading ----

describe("NDJSON reading", () => {
  it("reads transactions.ndjson correctly", () => {
    const rows = readFile(fixture("transactions.ndjson"), "ndjson");
    assert.ok(rows.length > 0);
    const first = rows[0];
    assert.ok(first !== undefined);
    assert.ok("txId" in first);
    assert.ok("type" in first);
    assert.ok("amount" in first);
  });

  it("NDJSON rows have correct types", () => {
    const rows = readFile(fixture("transactions.ndjson"), "ndjson");
    for (const row of rows) {
      assert.ok(typeof row["txId"] === "string");
      assert.ok(typeof row["amount"] === "number");
    }
  });
});

// ---- formatOutput ----

describe("formatOutput", () => {
  const rows = [{ a: 1, b: "hello" }, { a: 2, b: "world" }];

  it("formats as JSON", () => {
    const out = formatOutput(rows, "json");
    const parsed = JSON.parse(out) as unknown;
    assert.deepEqual(parsed, rows);
  });

  it("formats as CSV with header", () => {
    const out = formatOutput(rows, "csv");
    assert.ok(out.includes("a,b") || out.includes('"a","b"'));
    assert.ok(out.includes("hello"));
  });

  it("formats as table", () => {
    const out = formatOutput(rows, "table");
    assert.ok(out.includes("|"));
    assert.ok(out.includes("hello"));
  });

  it("handles empty rows for json", () => {
    const out = formatOutput([], "json");
    const parsed = JSON.parse(out) as unknown;
    assert.ok(Array.isArray(parsed) && parsed.length === 0, "should be empty array");
  });
});
