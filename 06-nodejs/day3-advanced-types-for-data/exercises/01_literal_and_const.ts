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

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - Status: union literal type of "pending" | "active" | "archived"
//   - HttpMethod: union literal type of "GET" | "POST" | "PUT" | "DELETE" | "PATCH"
//   - ROLES: const array of ["admin", "editor", "viewer"] (use `as const`)
//   - Role: type derived from ROLES using typeof + indexed access
//   - describeStatus(s: Status): string — returns a human-readable description
//   - isSafeMethod(method: HttpMethod): boolean — returns true only for "GET"
//   - hasWriteAccess(role: Role): boolean — returns true for "admin" or "editor"
//   - DEFAULT_REQUEST: const object with method "GET" and timeout 5000 (use `as const`)
//   - DefaultMethod: type derived from DEFAULT_REQUEST["method"]
//   - useDefaultMethod(m: DefaultMethod): string — returns `Using method: ${m}`

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
