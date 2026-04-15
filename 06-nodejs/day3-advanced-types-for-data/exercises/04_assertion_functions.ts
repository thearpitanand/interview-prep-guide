/**
 * Exercise 04 — Assertion Functions
 *
 * Topics:
 *   - `asserts x is T` — narrows type for all code after the call
 *   - `assertHasKey` — generic key check with `Record<K, unknown>`
 *   - Composing assertions to extract a nested unknown value safely
 */

import assert from "node:assert/strict";

// ── Assertion functions ────────────────────────────────────────────────────

export function assertIsNumber(x: unknown): asserts x is number { throw new TypeError("TODO: implement assertIsNumber"); }

export function assertIsString(x: unknown): asserts x is string { throw new TypeError("TODO: implement assertIsString"); }

export function assertHasKey<K extends string>(
  obj: unknown,
  key: K
): asserts obj is Record<K, unknown> { throw new TypeError("TODO: implement assertHasKey"); }

// ── Using assertions to extract a deeply nested value ─────────────────────

export function extractUserId(payload: unknown): number { throw new Error("TODO: implement extractUserId"); }

export function extractEventName(payload: unknown): string { throw new Error("TODO: implement extractEventName"); }

// ── Tests ─────────────────────────────────────────────────────────────────

const validPayload: unknown = JSON.parse('{"user": {"id": 42, "name": "Alice"}}');
assert.equal(extractUserId(validPayload), 42);

const eventPayload: unknown = JSON.parse('{"event": "purchase", "amount": 99.99}');
assert.equal(extractEventName(eventPayload), "purchase");

// assertIsNumber should throw on a string.
assert.throws(() => assertIsNumber("42"), TypeError);

// assertIsNumber should throw on NaN.
assert.throws(() => assertIsNumber(NaN), TypeError);

// assertHasKey should throw when key is missing.
assert.throws(() => assertHasKey({ a: 1 }, "b"), TypeError);

// extractUserId should throw when the nested path is wrong.
assert.throws(() => extractUserId({ user: { name: "Bob" } }), TypeError);

// assertIsString should throw on a number.
assert.throws(() => assertIsString(123), TypeError);

console.log("All tests passed!");
