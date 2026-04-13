/**
 * Day 1 — Exercise 01: Primitives and Inference
 *
 * Explore how TypeScript infers types for primitives, the difference between
 * let (widens) and const (narrows), and how as const pins literal types.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/01_primitives_and_inference.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

// Explicit type annotations
const userId: string = "u_001";
const transactionAmount: number = -49.99;
const isActive: boolean = true;
const maybeNull: null = null;
const notYet: undefined = undefined;

// Inferred types — TypeScript figures out the type from the initializer
const inferredString = "hello";     // inferred: "hello" (literal type, because const)
const inferredNumber = 42;          // inferred: 42 (literal type)
const inferredBool = false;         // inferred: false (literal type)

// let widens — the value might be reassigned to any other string
let mutableLabel = "pending";       // inferred: string (not literal "pending")
mutableLabel = "complete";          // legal — it's just string

// const narrows — TypeScript knows the value can never change
const STATUS_PENDING = "pending";   // inferred: "pending" (string literal type)

// Demonstrating the widening difference matters for union types
type Status = "pending" | "complete" | "failed";

function applyStatus(s: Status): string {
  return `status=${s}`;
}

// This works because STATUS_PENDING has literal type "pending"
const r1 = applyStatus(STATUS_PENDING);

// To use a let variable, cast it or use as const at the assignment
const dynamicStatus = "complete" as const;  // pins to literal "complete"
const r2 = applyStatus(dynamicStatus);

// as const on an object — all properties become readonly literal types
const defaultConfig = {
  host: "localhost",
  port: 5432,
  ssl: false,
} as const;
// defaultConfig.port has type 5432, not number

// as const on an array — becomes readonly tuple of literals
const VALID_CATEGORIES = ["groceries", "utilities", "transport", "dining"] as const;
// type: readonly ["groceries", "utilities", "transport", "dining"]

type Category = typeof VALID_CATEGORIES[number];
// type: "groceries" | "utilities" | "transport" | "dining"

function formatCategory(c: Category): string {
  return c.charAt(0).toUpperCase() + c.slice(1);
}

// bigint — for integers that exceed Number.MAX_SAFE_INTEGER
const bigBalance: bigint = 9_007_199_254_740_993n;

// ---------- TESTS ----------

assert.equal(userId, "u_001");
assert.equal(transactionAmount, -49.99);
assert.equal(isActive, true);
assert.equal(maybeNull, null);
assert.equal(notYet, undefined);

assert.equal(inferredString, "hello");
assert.equal(inferredNumber, 42);
assert.equal(inferredBool, false);

// let can be reassigned
assert.equal(mutableLabel, "complete");

// as const keeps literal type — value unchanged
assert.equal(STATUS_PENDING, "pending");
assert.equal(defaultConfig.host, "localhost");
assert.equal(defaultConfig.port, 5432);
assert.equal(defaultConfig.ssl, false);

// applyStatus returns the expected string
assert.equal(r1, "status=pending");
assert.equal(r2, "status=complete");

// formatCategory uppercases the first letter
assert.equal(formatCategory("groceries"), "Groceries");
assert.equal(formatCategory("transport"), "Transport");

// VALID_CATEGORIES is a readonly array with the right length
assert.equal(VALID_CATEGORIES.length, 4);
assert.equal(VALID_CATEGORIES[0], "groceries");

// bigint arithmetic
assert.equal(bigBalance + 1n, 9_007_199_254_740_994n);

console.log("All tests passed!");
