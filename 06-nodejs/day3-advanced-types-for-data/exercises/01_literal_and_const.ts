/**
 * Exercise 01 — Literal Types & `as const`
 *
 * Topics:
 *   - Union literal types for Status, Role, HttpMethod
 *   - `as const` to prevent widening
 *   - Deriving a type from a const array
 *   - Functions that accept only specific literal values
 */

import assert from "node:assert/strict";

// ── Literal union types ────────────────────────────────────────────────────

type Status = "pending" | "active" | "archived";
type HttpMethod = "GET" | "POST" | "PUT" | "DELETE" | "PATCH";

// Derive Role from a const array so the type and the source of truth stay in sync.
const ROLES = ["admin", "editor", "viewer"] as const;
type Role = (typeof ROLES)[number];

// ── Functions that accept only specific literals ───────────────────────────

function describeStatus(s: Status): string {
  if (s === "pending") return "Awaiting activation";
  if (s === "active") return "Currently active";
  return "No longer active";
}

function isSafeMethod(method: HttpMethod): boolean {
  return method === "GET";
}

function hasWriteAccess(role: Role): boolean {
  return role === "admin" || role === "editor";
}

// ── `as const` on an object literal ───────────────────────────────────────

const DEFAULT_REQUEST = {
  method: "GET",
  timeout: 5000,
} as const;

// Without `as const`, method would be widened to string.
// With it, TypeScript knows method is exactly "GET".
type DefaultMethod = (typeof DEFAULT_REQUEST)["method"]; // "GET"

function useDefaultMethod(m: DefaultMethod): string {
  return `Using method: ${m}`;
}

// ── Tests ─────────────────────────────────────────────────────────────────

assert.equal(describeStatus("pending"), "Awaiting activation");
assert.equal(describeStatus("active"), "Currently active");
assert.equal(describeStatus("archived"), "No longer active");

assert.equal(isSafeMethod("GET"), true);
assert.equal(isSafeMethod("POST"), false);
assert.equal(isSafeMethod("DELETE"), false);

assert.equal(hasWriteAccess("admin"), true);
assert.equal(hasWriteAccess("editor"), true);
assert.equal(hasWriteAccess("viewer"), false);

assert.equal(useDefaultMethod(DEFAULT_REQUEST.method), "Using method: GET");

// Verify ROLES array contains exactly the three expected values.
assert.deepEqual([...ROLES], ["admin", "editor", "viewer"]);

console.log("All tests passed!");
