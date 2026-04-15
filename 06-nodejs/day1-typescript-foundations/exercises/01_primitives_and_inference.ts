/**
 * Day 1 — Exercise 01: Primitives and Inference
 *
 * Explore how TypeScript infers types for primitives, the difference between
 * let (widens) and const (narrows), and how as const pins literal types.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/01_primitives_and_inference.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - userId: string                          — value "u_001"
//   - transactionAmount: number               — value -49.99
//   - isActive: boolean                       — value true
//   - maybeNull: null                         — value null
//   - notYet: undefined                       — value undefined
//   - inferredString                          — inferred string const, value "hello"
//   - inferredNumber                          — inferred number const, value 42
//   - inferredBool                            — inferred boolean const, value false
//   - mutableLabel (let)                      — reassigned to "complete" before tests
//   - STATUS_PENDING (const)                  — literal "pending"
//   - type Status                             — union "pending" | "complete" | "failed"
//   - function applyStatus(s: Status): string — returns `status=${s}`
//   - r1                                      — result of applyStatus(STATUS_PENDING)
//   - dynamicStatus                           — "complete" as const
//   - r2                                      — result of applyStatus(dynamicStatus)
//   - defaultConfig                           — as const object with host, port, ssl
//   - VALID_CATEGORIES                        — as const array of 4 category strings
//   - type Category                           — derived from typeof VALID_CATEGORIES[number]
//   - function formatCategory(c: Category): string — uppercases first letter
//   - bigBalance: bigint                      — value 9_007_199_254_740_993n
// Read the tests to infer expected values.

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
