/**
 * Exercise 02 — Flatten and Unflatten Nested Objects
 *
 * Topics: recursive object traversal, dot-path keys, round-trip correctness
 *
 * Strategy for arrays: leave them in-place (do not recurse into array elements).
 * This is the right default for ETL — arrays represent collections, not
 * sub-structures. Keys like "tags.0" are almost never what you want.
 *
 * Tasks:
 *   1. Implement `flatten(obj, sep?)` — nested object → dot-path keys.
 *   2. Implement `unflatten(flat, sep?)` — dot-path keys → nested object.
 *   3. Verify round-trip: unflatten(flatten(obj)) deep-equals obj.
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// 1. flatten
// ---------------------------------------------------------------------------

export function flatten(
  obj: Record<string, unknown>,
  sep = ".",
  prefix = ""
): Record<string, unknown> {
  throw new Error("TODO: implement flatten");
}

// ---------------------------------------------------------------------------
// 2. unflatten
// ---------------------------------------------------------------------------

export function unflatten(
  flat: Record<string, unknown>,
  sep = "."
): Record<string, unknown> {
  throw new Error("TODO: implement unflatten");
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  // --- Flat object — no nesting ---
  const flat1 = { name: "Ava", age: 30 };
  assert.deepEqual(flatten(flat1), { name: "Ava", age: 30 });
  assert.deepEqual(unflatten(flatten(flat1)), flat1);

  // --- One level of nesting ---
  const nested1 = { address: { city: "London", zip: "EC1A" } };
  assert.deepEqual(flatten(nested1), {
    "address.city": "London",
    "address.zip": "EC1A",
  });
  assert.deepEqual(unflatten(flatten(nested1)), nested1);

  // --- Two levels of nesting ---
  const nested2 = { a: { b: { c: 1 } }, d: 2 };
  assert.deepEqual(flatten(nested2), { "a.b.c": 1, d: 2 });
  assert.deepEqual(unflatten(flatten(nested2)), nested2);

  // --- Mixed: primitives + nested + arrays ---
  const mixed = {
    id: "C001",
    name: "Ava",
    address: { city: "Paris", country: "FR" },
    tags: ["gold", "vip"],   // array — stays in place
    score: null,
  };
  const flatMixed = flatten(mixed);
  assert.deepEqual(flatMixed, {
    id: "C001",
    name: "Ava",
    "address.city": "Paris",
    "address.country": "FR",
    tags: ["gold", "vip"],
    score: null,
  });
  assert.deepEqual(unflatten(flatMixed), mixed);

  // --- Custom separator ---
  const withCustomSep = flatten({ a: { b: 1 } }, "_");
  assert.deepEqual(withCustomSep, { a_b: 1 });
  assert.deepEqual(unflatten(withCustomSep, "_"), { a: { b: 1 } });

  // --- Empty object ---
  assert.deepEqual(flatten({}), {});
  assert.deepEqual(unflatten({}), {});

  // --- Deeply nested (3 levels) ---
  const deep = { x: { y: { z: { w: 42 } } } };
  assert.deepEqual(flatten(deep), { "x.y.z.w": 42 });
  assert.deepEqual(unflatten(flatten(deep)), deep);

  // --- Multiple keys at same nesting level ---
  const wide = {
    user: { firstName: "Bob", lastName: "Smith" },
    meta: { createdAt: "2024-01-01", version: 3 },
  };
  assert.deepEqual(flatten(wide), {
    "user.firstName": "Bob",
    "user.lastName": "Smith",
    "meta.createdAt": "2024-01-01",
    "meta.version": 3,
  });
  assert.deepEqual(unflatten(flatten(wide)), wide);

  // --- Boolean values ---
  const withBool = { config: { enabled: true, debug: false } };
  assert.deepEqual(flatten(withBool), { "config.enabled": true, "config.debug": false });
  assert.deepEqual(unflatten(flatten(withBool)), withBool);

  console.log("All tests passed!");
}
