/**
 * Day 1 — Exercise 02: Objects and Interfaces
 *
 * Define a User interface with optional and readonly properties, write
 * functions that operate on it, and demonstrate index signatures.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/02_objects_and_interfaces.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - interface User                                   — with id: string, email: string,
//                                                        displayName?: string, readonly createdAt: Date
//   - function greetUser(user: User): string           — returns "Hello, <displayName or email>!"
//   - function formatUserSummary(user: User): string   — returns a line containing id, email,
//                                                        display name (or "(no display name)"),
//                                                        and join date (YYYY-MM-DD)
//   - interface MetadataMap                            — index signature [key: string]: string
//   - function buildMetadata(pairs: [string, string][]): MetadataMap
//                                                      — builds a map from key-value pair tuples
//   - userAlice: User                                  — id "u_001", email "alice@example.com",
//                                                        displayName "Alice Chen", createdAt 2024-01-15
//   - userBob: User                                    — id "u_002", email "bob@example.com",
//                                                        no displayName, createdAt 2024-03-20
// Read the tests to infer expected values.

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
