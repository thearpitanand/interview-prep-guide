/**
 * Day 1 — Exercise 03: Arrays and Tuples
 *
 * Practice typed array operations (map/filter/reduce), define and use tuple
 * types, and work with readonly arrays safely under noUncheckedIndexedAccess.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/03_arrays_and_tuples.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

// Typed array — all elements must be numbers
const amounts: number[] = [120.5, -45.0, 200.0, -30.75, 88.25, -15.0];

// map: transform every element — return type is inferred as number[]
const absAmounts: number[] = amounts.map((n) => Math.abs(n));

// filter: keep only positives — return type is number[]
const income: number[] = amounts.filter((n) => n > 0);

// filter: keep only negatives
const expenses: number[] = amounts.filter((n) => n < 0);

// reduce: sum all values
const total: number = amounts.reduce((acc, n) => acc + n, 0);

// A function that computes stats using readonly input — cannot mutate the array
function summarize(values: readonly number[]): {
  count: number;
  sum: number;
  min: number;
  max: number;
} {
  if (values.length === 0) {
    return { count: 0, sum: 0, min: 0, max: 0 };
  }

  let sum = 0;
  let min = Infinity;
  let max = -Infinity;

  for (const v of values) {
    sum += v;
    if (v < min) min = v;
    if (v > max) max = v;
  }

  return { count: values.length, sum, min, max };
}

// Tuple type — fixed positions with known types
type NameAmountPair = [string, number];

// A function that parses a "description:amount" string into a tuple
function parseEntry(raw: string): NameAmountPair {
  const colonIndex = raw.indexOf(":");
  if (colonIndex === -1) {
    throw new Error(`Invalid entry format: ${raw}`);
  }
  const name = raw.slice(0, colonIndex).trim();
  const amount = parseFloat(raw.slice(colonIndex + 1).trim());
  return [name, amount];
}

// Destructuring a tuple
const [label, value] = parseEntry("Groceries: -52.30");

// A function returning a tuple for min/max
function minMax(values: readonly number[]): [number, number] {
  if (values.length === 0) {
    throw new Error("Cannot compute minMax of empty array");
  }
  let lo = Infinity;
  let hi = -Infinity;
  for (const v of values) {
    if (v < lo) lo = v;
    if (v > hi) hi = v;
  }
  return [lo, hi];
}

const [lo, hi] = minMax(amounts);

// noUncheckedIndexedAccess — arr[i] is T | undefined, must narrow before use
const tags: string[] = ["urgent", "reviewed", "archived"];
const firstTag = tags[0];  // type: string | undefined

const displayTag: string = firstTag !== undefined ? firstTag : "untagged";

// for..of is always safe — no T | undefined here
const upperTags: string[] = [];
for (const tag of tags) {
  upperTags.push(tag.toUpperCase());
}

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
