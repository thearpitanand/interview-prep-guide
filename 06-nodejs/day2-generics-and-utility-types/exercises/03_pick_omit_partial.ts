/**
 * Day 2 — Exercise 03: Pick, Omit, and Partial
 *
 * Given a User type, derive PublicUser, UserPatch, and CreateUserInput
 * using built-in utility types. Implement patchUser using Partial<User>.
 *
 * Run: npx tsx day2-generics-and-utility-types/exercises/03_pick_omit_partial.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

interface User {
  id: string;
  name: string;
  email: string;
  passwordHash: string;
  role: "admin" | "user";
  createdAt: Date;
}

// Only expose safe public fields
type PublicUser = Omit<User, "passwordHash">;

// All fields optional for PATCH requests
type UserPatch = Partial<User>;

// Omit the auto-generated fields for creation
type CreateUserInput = Omit<User, "id" | "createdAt">;

/**
 * Apply a partial patch to a user, returning a new User object.
 * Only the provided fields are overwritten; the rest stay as-is.
 */
function patchUser(user: User, patch: Partial<User>): User {
  return { ...user, ...patch };
}

/**
 * Strip the passwordHash before sending user data out of the system.
 */
function toPublicUser(user: User): PublicUser {
  const { passwordHash: _ignored, ...rest } = user;
  return rest;
}

// ---------- TESTS ----------

const now = new Date("2024-01-01");
const base: User = {
  id: "u-1",
  name: "Alice",
  email: "alice@example.com",
  passwordHash: "hashed_secret",
  role: "user",
  createdAt: now,
};

// patchUser — update name
const patched1 = patchUser(base, { name: "Alicia" });
assert.equal(patched1.name, "Alicia");
assert.equal(patched1.email, "alice@example.com");  // unchanged
assert.equal(patched1.id, "u-1");                   // unchanged

// patchUser — update role
const patched2 = patchUser(base, { role: "admin" });
assert.equal(patched2.role, "admin");

// patchUser — empty patch returns equivalent object
const patched3 = patchUser(base, {});
assert.deepEqual(patched3, base);

// patchUser — original is not mutated
assert.equal(base.name, "Alice");
assert.equal(base.role, "user");

// toPublicUser — passwordHash is absent
const pub = toPublicUser(base);
assert.equal("passwordHash" in pub, false);
assert.equal(pub.name, "Alice");
assert.equal(pub.email, "alice@example.com");
assert.equal(pub.role, "user");

// CreateUserInput shape — verify at type level by constructing one
const input: CreateUserInput = {
  name: "Bob",
  email: "bob@example.com",
  passwordHash: "some_hash",
  role: "user",
};
assert.equal(input.name, "Bob");

console.log("All tests passed!");
