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
export function buildProfile(userId: string, displayName: string, age: number) {
  throw new Error("TODO: implement buildProfile");
}

// TODO: derive Profile from the return type of buildProfile (no manual shape)
type Profile = unknown; // TODO: define Profile using ReturnType<...>

// TODO: derive BuildProfileParams from the parameter tuple of buildProfile
type BuildProfileParams = unknown; // TODO: define BuildProfileParams using Parameters<...>

/**
 * A wrapper that calls buildProfile but logs the arguments first.
 * Uses the derived Parameters type so the signature stays in sync automatically.
 */
export function buildProfileWithLog(...args: Parameters<typeof buildProfile>): ReturnType<typeof buildProfile> {
  throw new Error("TODO: implement buildProfileWithLog");
}

// ---------- Awaited demonstration ----------

// An async function that resolves to a number
export async function fetchScore(userId: string): Promise<number> {
  throw new Error("TODO: implement fetchScore");
}

// TODO: derive Score — unwrap the Promise return type of fetchScore
type Score = unknown; // TODO: define Score using Awaited<ReturnType<...>>

// TODO: define NestedP as Promise<Promise<string>> and UnwrappedNested as Awaited<NestedP>
type NestedP = unknown; // TODO: define NestedP
type UnwrappedNested = unknown; // TODO: define UnwrappedNested

// Use Awaited in a generic helper
export function resolveWith<T>(value: Awaited<Promise<T>>): T {
  throw new Error("TODO: implement resolveWith");
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
