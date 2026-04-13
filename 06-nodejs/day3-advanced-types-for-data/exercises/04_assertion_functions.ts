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

function assertIsNumber(x: unknown): asserts x is number {
  if (typeof x !== "number" || Number.isNaN(x)) {
    throw new TypeError(`Expected number, got ${typeof x}`);
  }
}

function assertIsString(x: unknown): asserts x is string {
  if (typeof x !== "string") {
    throw new TypeError(`Expected string, got ${typeof x}`);
  }
}

function assertHasKey<K extends string>(
  obj: unknown,
  key: K
): asserts obj is Record<K, unknown> {
  if (typeof obj !== "object" || obj === null || !(key in obj)) {
    throw new TypeError(`Expected object with key "${key}"`);
  }
}

// ── Using assertions to extract a deeply nested value ─────────────────────

function extractUserId(payload: unknown): number {
  assertHasKey(payload, "user");
  assertHasKey(payload["user"], "id");
  assertIsNumber(payload["user"]["id"]);
  // After all three assertions, TypeScript knows payload["user"]["id"] is number.
  return payload["user"]["id"];
}

function extractEventName(payload: unknown): string {
  assertHasKey(payload, "event");
  assertIsString(payload["event"]);
  return payload["event"];
}

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
