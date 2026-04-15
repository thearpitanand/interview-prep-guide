/**
 * Day 1 — Exercise 03: Arrays and Tuples
 *
 * Practice typed array operations (map/filter/reduce), define and use tuple
 * types, and work with readonly arrays safely under noUncheckedIndexedAccess.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/03_arrays_and_tuples.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - amounts: number[]                  — [120.5, -45.0, 200.0, -30.75, 88.25, -15.0]
//   - absAmounts: number[]               — absolute values of amounts (via map)
//   - income: number[]                   — only positive values from amounts (via filter)
//   - expenses: number[]                 — only negative values from amounts (via filter)
//   - total: number                      — sum of all amounts (via reduce)
//   - function summarize(values: readonly number[]): { count, sum, min, max }
//                                        — returns stats; returns all-zeros for empty array
//   - type NameAmountPair                — tuple type [string, number]
//   - function parseEntry(raw: string): NameAmountPair
//                                        — parses "Description: amount" format
//   - [label, value]                     — destructured result of parseEntry("Groceries: -52.30")
//   - function minMax(values: readonly number[]): [number, number]
//                                        — returns [min, max]; throws if empty
//   - [lo, hi]                           — destructured result of minMax(amounts)
//   - tags: string[]                     — ["urgent", "reviewed", "archived"]
//   - firstTag                           — tags[0] (type: string | undefined)
//   - displayTag: string                 — firstTag if defined, else "untagged"
//   - upperTags: string[]                — tags mapped to uppercase via for..of
// Read the tests to infer expected values.

// ---------- TESTS ----------

assert.equal(amounts.length, 6);

// map produces absolute values
assert.ok(absAmounts.every((n) => n >= 0));
assert.equal(absAmounts[0], 120.5);

// filter splits correctly
assert.equal(income.length, 3);
assert.ok(income.every((n) => n > 0));

assert.equal(expenses.length, 3);
assert.ok(expenses.every((n) => n < 0));

// reduce total (allow small float epsilon)
assert.ok(Math.abs(total - 318.0) < 0.001);

// summarize handles a normal array
const stats = summarize(amounts);
assert.equal(stats.count, 6);
assert.ok(Math.abs(stats.sum - 318.0) < 0.001);
assert.equal(stats.min, -45.0);
assert.equal(stats.max, 200.0);

// summarize handles empty array
const emptyStats = summarize([]);
assert.equal(emptyStats.count, 0);
assert.equal(emptyStats.sum, 0);

// tuple destructuring
assert.equal(label, "Groceries");
assert.ok(Math.abs(value - (-52.30)) < 0.001);

// minMax
assert.equal(lo, -45.0);
assert.equal(hi, 200.0);

// noUncheckedIndexedAccess — narrowed correctly
assert.equal(displayTag, "urgent");

// for..of uppercasing
assert.deepEqual(upperTags, ["URGENT", "REVIEWED", "ARCHIVED"]);

console.log("All tests passed!");
