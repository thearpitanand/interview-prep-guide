/**
 * Day 2 — Exercise 04: Record and keyof
 *
 * Build a word-frequency counter using Record<string, number> and a
 * generic groupBy function using Record with a constrained key type.
 *
 * Run: npx tsx day2-generics-and-utility-types/exercises/04_record_and_keyof.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

/**
 * Count occurrences of each word in the input array.
 * Returns a Record<string, number> mapping word -> count.
 */
function countWords(words: string[]): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const word of words) {
    counts[word] = (counts[word] ?? 0) + 1;
  }
  return counts;
}

/**
 * Group an array of T by the string key returned by fn.
 * K is constrained to string so it can serve as an object key.
 */
function groupBy<T, K extends string>(
  arr: T[],
  fn: (t: T) => K
): Record<K, T[]> {
  const result = {} as Record<K, T[]>;
  for (const item of arr) {
    const key = fn(item);
    if (result[key] === undefined) {
      result[key] = [];
    }
    result[key].push(item);
  }
  return result;
}

// ---------- TESTS ----------

// countWords — basic frequency count
const words = ["apple", "banana", "apple", "cherry", "banana", "apple"];
const freq = countWords(words);
assert.equal(freq["apple"], 3);
assert.equal(freq["banana"], 2);
assert.equal(freq["cherry"], 1);

// countWords — empty array
const emptyFreq = countWords([]);
assert.deepEqual(emptyFreq, {});

// countWords — single word
const single = countWords(["only"]);
assert.equal(single["only"], 1);

// groupBy — group people by department
interface Employee {
  name: string;
  dept: "eng" | "design" | "product";
}

const employees: Employee[] = [
  { name: "Alice", dept: "eng" },
  { name: "Bob",   dept: "design" },
  { name: "Carol", dept: "eng" },
  { name: "Dave",  dept: "product" },
  { name: "Eve",   dept: "design" },
];

const byDept = groupBy(employees, (e) => e.dept);
assert.equal(byDept["eng"].length, 2);
assert.equal(byDept["design"].length, 2);
assert.equal(byDept["product"].length, 1);
assert.equal(byDept["eng"][0]?.name, "Alice");

// groupBy — group numbers by even/odd
const nums = [1, 2, 3, 4, 5, 6];
const byParity = groupBy(nums, (n) => (n % 2 === 0 ? "even" : "odd"));
assert.equal(byParity["even"].length, 3);
assert.equal(byParity["odd"].length, 3);

// groupBy — single item
const one = groupBy([42], (n) => "only");
assert.deepEqual(one["only"], [42]);

console.log("All tests passed!");
