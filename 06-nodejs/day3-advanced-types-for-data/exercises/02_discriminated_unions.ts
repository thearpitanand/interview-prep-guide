/**
 * Exercise 02 — Discriminated Unions
 *
 * Topics:
 *   - Tagged union with a `level` discriminant
 *   - Exhaustive switch with `never` default
 *   - `assertNever` helper
 */

import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - LogEntry: discriminated union with variants:
//       { level: "info";  message: string }
//       { level: "warn";  message: string; code: number }
//       { level: "error"; message: string; error: Error }
//   - assertNever(x: never): never — throws an error (ensures exhaustive switches)
//   - formatEntry(e: LogEntry): string — formats each variant:
//       "info"  → "[INFO]  <message>"
//       "warn"  → "[WARN]  <message> (code <code>)"
//       "error" → "[ERROR] <message>: <error.message>"
//   - severity(e: LogEntry): number — 0 for info, 1 for warn, 2 for error

// ── Tests ─────────────────────────────────────────────────────────────────

const info: LogEntry  = { level: "info",  message: "Server started" };
const warn: LogEntry  = { level: "warn",  message: "High memory", code: 503 };
const error: LogEntry = { level: "error", message: "Crash", error: new Error("OOM") };

assert.equal(formatEntry(info),  "[INFO]  Server started");
assert.equal(formatEntry(warn),  "[WARN]  High memory (code 503)");
assert.equal(formatEntry(error), "[ERROR] Crash: OOM");

assert.equal(severity(info),  0);
assert.equal(severity(warn),  1);
assert.equal(severity(error), 2);

// Sorting entries by severity should put info first, error last.
const entries: LogEntry[] = [error, info, warn];
const sorted = [...entries].sort((a, b) => severity(a) - severity(b));
assert.equal(sorted[0]?.level, "info");
assert.equal(sorted[1]?.level, "warn");
assert.equal(sorted[2]?.level, "error");

console.log("All tests passed!");
