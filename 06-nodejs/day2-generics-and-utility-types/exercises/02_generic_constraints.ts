/**
 * Day 2 — Exercise 02: Generic Constraints
 *
 * Implement pluck, pickKeys, and maxBy using keyof constraints.
 * Each function's return type must be inferred precisely from the inputs.
 *
 * Run: npx tsx day2-generics-and-utility-types/exercises/02_generic_constraints.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

/**
 * Return obj[key], preserving the exact type of that property.
 */
export function pluck<T, K extends keyof T>(obj: T, key: K): T[K] {
  throw new Error("TODO: implement pluck");
}

/**
 * Return a new object containing only the specified keys from obj.
 */
export function pickKeys<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
  throw new Error("TODO: implement pickKeys");
}

/**
 * Return the element in arr for which fn returns the highest number.
 * Returns undefined if the array is empty.
 */
export function maxBy<T>(arr: T[], fn: (t: T) => number): T | undefined {
  throw new Error("TODO: implement maxBy");
}

// ---------- TESTS ----------

interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

const alice: User = { id: 1, name: "Alice", email: "alice@example.com", age: 30 };
const bob:   User = { id: 2, name: "Bob",   email: "bob@example.com",   age: 25 };
const carol: User = { id: 3, name: "Carol", email: "carol@example.com", age: 35 };

// pluck — exact type preservation
const name = pluck(alice, "name");
assert.equal(name, "Alice");

const id = pluck(alice, "id");
assert.equal(id, 1);

const email = pluck(bob, "email");
assert.equal(email, "bob@example.com");

// pickKeys — resulting object has only the requested keys
const publicAlice = pickKeys(alice, ["id", "name"]);
assert.deepEqual(publicAlice, { id: 1, name: "Alice" });
assert.equal(Object.keys(publicAlice).length, 2);

const contactBob = pickKeys(bob, ["name", "email"]);
assert.deepEqual(contactBob, { name: "Bob", email: "bob@example.com" });

// maxBy — find user with highest age
const users = [alice, bob, carol];
const oldest = maxBy(users, (u) => u.age);
assert.equal(oldest?.name, "Carol");

// maxBy — lowest id (invert with negation)
const lowestId = maxBy(users, (u) => -u.id);
assert.equal(lowestId?.id, 1);

// maxBy — empty array returns undefined
const none = maxBy<User>([], (u) => u.age);
assert.equal(none, undefined);

// maxBy — numbers array
const scores = [3, 7, 1, 9, 4];
const highest = maxBy(scores, (n) => n);
assert.equal(highest, 9);

console.log("All tests passed!");
