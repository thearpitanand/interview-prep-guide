/**
 * Exercise 03 — Type Guards
 *
 * Topics:
 *   - User-defined type predicates: `x is T`
 *   - Filtering unknown[] to a typed array
 *   - Narrowing with `isNonEmptyString`
 *   - Guard that checks nested structure
 */

import assert from "node:assert/strict";

// ── Domain types ───────────────────────────────────────────────────────────

type User = { id: number; name: string; email: string };

type Product = { sku: string; price: number };

// ── Type guards ────────────────────────────────────────────────────────────

function isUser(x: unknown): x is User {
  if (typeof x !== "object" || x === null) return false;
  const obj = x as Record<string, unknown>;
  return (
    typeof obj["id"]    === "number" &&
    typeof obj["name"]  === "string" &&
    typeof obj["email"] === "string"
  );
}

function isProduct(x: unknown): x is Product {
  if (typeof x !== "object" || x === null) return false;
  const obj = x as Record<string, unknown>;
  return (
    typeof obj["sku"]   === "string" &&
    typeof obj["price"] === "number"
  );
}

function isNonEmptyString(x: unknown): x is string {
  return typeof x === "string" && x.length > 0;
}

// ── Functions using the guards ─────────────────────────────────────────────

function extractUsers(items: unknown[]): User[] {
  return items.filter(isUser);
}

function getDisplayName(x: unknown): string {
  if (isUser(x)) return x.name;
  if (isNonEmptyString(x)) return x;
  return "(unknown)";
}

// ── Tests ─────────────────────────────────────────────────────────────────

const mixed: unknown[] = [
  { id: 1, name: "Alice",   email: "alice@example.com" },
  { id: 2, name: "Bob",     email: "bob@example.com" },
  { sku: "ABC-1", price: 9.99 },
  "not an object",
  null,
  42,
  { id: "bad", name: "Charlie", email: "c@example.com" }, // id is string, not number
];

const users = extractUsers(mixed);
assert.equal(users.length, 2);
assert.equal(users[0]?.name, "Alice");
assert.equal(users[1]?.name, "Bob");

assert.equal(isUser(mixed[0]), true);
assert.equal(isUser(mixed[2]), false);  // Product, not User
assert.equal(isUser(null),     false);
assert.equal(isUser("string"), false);

assert.equal(isProduct(mixed[2]), true);
assert.equal(isProduct(mixed[0]), false);

assert.equal(isNonEmptyString("hello"), true);
assert.equal(isNonEmptyString(""),      false);
assert.equal(isNonEmptyString(42),      false);

const alice = mixed[0];
assert.equal(getDisplayName(alice), "Alice");
assert.equal(getDisplayName("Bob"), "Bob");
assert.equal(getDisplayName(null),  "(unknown)");

console.log("All tests passed!");
