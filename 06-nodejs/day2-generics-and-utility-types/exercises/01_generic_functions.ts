/**
 * Day 2 — Exercise 01: Generic Functions
 *
 * Implement first, last, identity, and pair as generic functions.
 * The return types must preserve the element type exactly.
 *
 * Run: npx tsx day2-generics-and-utility-types/exercises/01_generic_functions.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

export function first<T>(arr: T[]): T | undefined {
  throw new Error("TODO: implement first");
}

export function last<T>(arr: T[]): T | undefined {
  throw new Error("TODO: implement last");
}

export function identity<T>(x: T): T {
  throw new Error("TODO: implement identity");
}

export function pair<A, B>(a: A, b: B): [A, B] {
  throw new Error("TODO: implement pair");
}

// ---------- TESTS ----------

// first — numbers
const nums = [10, 20, 30];
const f1 = first(nums);
assert.equal(f1, 10);

// first — strings
const strs = ["alpha", "beta", "gamma"];
const f2 = first(strs);
assert.equal(f2, "alpha");

// first — empty array returns undefined
const f3 = first<number>([]);
assert.equal(f3, undefined);

// last — numbers
const l1 = last(nums);
assert.equal(l1, 30);

// last — strings
const l2 = last(strs);
assert.equal(l2, "gamma");

// last — empty array returns undefined
const l3 = last<string>([]);
assert.equal(l3, undefined);

// identity — number
const i1 = identity(42);
assert.equal(i1, 42);

// identity — object reference
const obj = { x: 1, y: 2 };
const i2 = identity(obj);
assert.equal(i2, obj); // same reference

// pair — mixed types
const p1 = pair(1, "one");
assert.deepEqual(p1, [1, "one"]);

// pair — boolean and array
const p2 = pair(true, [1, 2, 3]);
assert.deepEqual(p2, [true, [1, 2, 3]]);

// pair — verifying each slot is correct
const p3 = pair("key", { value: 99 });
assert.equal(p3[0], "key");
assert.equal(p3[1].value, 99);

console.log("All tests passed!");
