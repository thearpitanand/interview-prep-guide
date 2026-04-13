/**
 * Day 1 — Exercise 02: Objects and Interfaces
 *
 * Define a User interface with optional and readonly properties, write
 * functions that operate on it, and demonstrate index signatures.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/02_objects_and_interfaces.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

interface User {
  id: string;
  email: string;
  displayName?: string;         // optional: string | undefined
  readonly createdAt: Date;     // cannot be reassigned after creation
}

// A function that returns a greeting using the User shape
function greetUser(user: User): string {
  // displayName is string | undefined — use nullish coalescing to provide a fallback
  const name = user.displayName ?? user.email;
  return `Hello, ${name}!`;
}

// A function that formats a user's account summary line
function formatUserSummary(user: User): string {
  const displayName = user.displayName ?? "(no display name)";
  const created = user.createdAt.toISOString().slice(0, 10);
  return `[${user.id}] ${user.email} | ${displayName} | joined ${created}`;
}

// An index signature — useful when property names are dynamic
interface MetadataMap {
  [key: string]: string;
}

function buildMetadata(pairs: [string, string][]): MetadataMap {
  const result: MetadataMap = {};
  for (const [k, v] of pairs) {
    result[k] = v;
  }
  return result;
}

// Two test users
const userAlice: User = {
  id: "u_001",
  email: "alice@example.com",
  displayName: "Alice Chen",
  createdAt: new Date("2024-01-15"),
};

const userBob: User = {
  id: "u_002",
  email: "bob@example.com",
  // displayName omitted — optional
  createdAt: new Date("2024-03-20"),
};

// ---------- TESTS ----------

// greetUser uses displayName when present
assert.equal(greetUser(userAlice), "Hello, Alice Chen!");

// greetUser falls back to email when displayName is absent
assert.equal(greetUser(userBob), "Hello, bob@example.com!");

// formatUserSummary includes id, email, and join date
assert.ok(formatUserSummary(userAlice).includes("u_001"));
assert.ok(formatUserSummary(userAlice).includes("alice@example.com"));
assert.ok(formatUserSummary(userAlice).includes("2024-01-15"));

// formatUserSummary shows "(no display name)" for Bob
assert.ok(formatUserSummary(userBob).includes("(no display name)"));

// optional property is undefined when not provided
assert.equal(userBob.displayName, undefined);

// readonly property holds the correct date
assert.equal(userAlice.createdAt.getFullYear(), 2024);

// index signature stores and retrieves values
const meta = buildMetadata([
  ["source", "import"],
  ["region", "us-west"],
]);
assert.equal(meta["source"], "import");
assert.equal(meta["region"], "us-west");

// reading a missing key from an index signature gives undefined (noUncheckedIndexedAccess)
const missing = meta["nonexistent"];
assert.equal(missing, undefined);

console.log("All tests passed!");
