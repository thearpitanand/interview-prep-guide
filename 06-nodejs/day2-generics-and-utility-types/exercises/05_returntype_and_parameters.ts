/**
 * Day 2 — Exercise 05: ReturnType, Parameters, and Awaited
 *
 * Derive function types with ReturnType and Parameters, build a wrapper
 * that passes args through unchanged, and unwrap Promise types with Awaited.
 *
 * Run: npx tsx day2-generics-and-utility-types/exercises/05_returntype_and_parameters.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

// A real function whose return type we want to derive
function buildProfile(userId: string, displayName: string, age: number) {
  return {
    id: userId,
    displayName,
    age,
    slug: displayName.toLowerCase().replace(/\s+/g, "-"),
    createdAt: new Date("2024-01-01"),
  };
}

// Derive the return type without repeating the shape
type Profile = ReturnType<typeof buildProfile>;

// Derive the parameter tuple
type BuildProfileParams = Parameters<typeof buildProfile>;

/**
 * A wrapper that calls buildProfile but logs the arguments first.
 * Uses the derived Parameters type so the signature stays in sync automatically.
 */
function buildProfileWithLog(...args: Parameters<typeof buildProfile>): ReturnType<typeof buildProfile> {
  console.log(`Building profile for: ${args[0]}`);
  return buildProfile(...args);
}

// ---------- Awaited demonstration ----------

// An async function that resolves to a number
async function fetchScore(userId: string): Promise<number> {
  // In real code this would be a network call
  return Promise.resolve(userId.length * 10);
}

// Unwrap the Promise type
type Score = Awaited<ReturnType<typeof fetchScore>>; // number

// Demonstrate Awaited works with nested promises too
type NestedP = Promise<Promise<string>>;
type UnwrappedNested = Awaited<NestedP>; // string

// Use Awaited in a generic helper
function resolveWith<T>(value: Awaited<Promise<T>>): T {
  return value;
}

// ---------- TESTS ----------

// buildProfile — correct return shape
const profile = buildProfile("u-1", "Alice Smith", 30);
assert.equal(profile.id, "u-1");
assert.equal(profile.displayName, "Alice Smith");
assert.equal(profile.age, 30);
assert.equal(profile.slug, "alice-smith");

// buildProfileWithLog — same result as buildProfile
const profileLogged = buildProfileWithLog("u-2", "Bob Jones", 25);
assert.equal(profileLogged.id, "u-2");
assert.equal(profileLogged.displayName, "Bob Jones");
assert.equal(profileLogged.slug, "bob-jones");

// Profile type usage — can assign buildProfile result to Profile
const p: Profile = buildProfile("u-3", "Carol", 40);
assert.equal(p.age, 40);

// BuildProfileParams usage — can build args tuple and spread it
const params: BuildProfileParams = ["u-4", "Dave", 22];
const fromParams = buildProfile(...params);
assert.equal(fromParams.id, "u-4");

// Awaited — async function resolves correctly
const score = await fetchScore("hello");
assert.equal(score, 50); // "hello".length * 10 = 5 * 10

// resolveWith — passes through correctly
const n: Score = resolveWith<number>(42);
assert.equal(n, 42);

console.log("All tests passed!");
