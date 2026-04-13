/**
 * Exercise 06 — `unknown` vs `any`
 *
 * Topics:
 *   - Why `any` is dangerous (silently bypasses the type system)
 *   - Using `unknown` at the boundary forces narrowing
 *   - Step-by-step narrowing from `unknown` to a typed `Transaction`
 *   - The parse-then-narrow pattern
 */

import assert from "node:assert/strict";

// ── Domain type ────────────────────────────────────────────────────────────

type Transaction = {
  id: string;
  amount: number;
  currency: string;
  status: "pending" | "settled" | "failed";
};

// ── Guard that checks every field ─────────────────────────────────────────

function isTransaction(x: unknown): x is Transaction {
  if (typeof x !== "object" || x === null) return false;
  const obj = x as Record<string, unknown>;
  return (
    typeof obj["id"]       === "string" &&
    typeof obj["amount"]   === "number" &&
    typeof obj["currency"] === "string" &&
    (obj["status"] === "pending" || obj["status"] === "settled" || obj["status"] === "failed")
  );
}

// ── Parse-then-narrow: the correct pattern ────────────────────────────────

function parseTransaction(raw: unknown): Transaction {
  if (!isTransaction(raw)) {
    throw new TypeError(`Invalid transaction: ${JSON.stringify(raw)}`);
  }
  return raw;
}

// ── Demonstrate why unknown is safer than any ─────────────────────────────
//
// With `any`:
//   const bad: any = JSON.parse(text);
//   bad.amount.toFixed(2);   <- no error even if amount is undefined
//
// With `unknown` you MUST narrow:
//   const safe: unknown = JSON.parse(text);
//   safe.amount;  <- ERROR: Object is of type 'unknown'
//   // only after isTransaction(safe) does safe.amount become number

// ── Tests ─────────────────────────────────────────────────────────────────

const validJson = '{"id":"tx-001","amount":49.99,"currency":"USD","status":"settled"}';
const raw: unknown = JSON.parse(validJson);

const tx = parseTransaction(raw);
assert.equal(tx.id, "tx-001");
assert.equal(tx.amount, 49.99);
assert.equal(tx.currency, "USD");
assert.equal(tx.status, "settled");

// amount is a number, so arithmetic is safe after narrowing.
assert.equal(tx.amount.toFixed(2), "49.99");

// parseTransaction should throw on bad data.
assert.throws(() => parseTransaction({ id: 1, amount: "bad", currency: "USD", status: "settled" }), TypeError);
assert.throws(() => parseTransaction(null), TypeError);
assert.throws(() => parseTransaction("string"), TypeError);

// isTransaction correctly rejects partial objects.
assert.equal(isTransaction({ id: "x", amount: 10 }), false); // missing currency, status
assert.equal(isTransaction({ id: "x", amount: 10, currency: "EUR", status: "unknown" }), false); // bad status

// isTransaction accepts a valid object.
assert.equal(isTransaction({ id: "x", amount: 10, currency: "EUR", status: "pending" }), true);

console.log("All tests passed!");
