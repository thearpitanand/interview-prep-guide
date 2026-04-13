/**
 * Exercise 02 — Discriminated Unions
 *
 * Topics:
 *   - Tagged union with a `level` discriminant
 *   - Exhaustive switch with `never` default
 *   - `assertNever` helper
 */

import assert from "node:assert/strict";

// ── Types ──────────────────────────────────────────────────────────────────

type LogEntry =
  | { level: "info";  message: string }
  | { level: "warn";  message: string; code: number }
  | { level: "error"; message: string; error: Error };

// ── assertNever ensures the switch is exhaustive ───────────────────────────

function assertNever(x: never): never {
  throw new Error(`Unhandled log level: ${JSON.stringify(x)}`);
}

// ── Business logic narrowed by the discriminant ───────────────────────────

function formatEntry(e: LogEntry): string {
  switch (e.level) {
    case "info":
      return `[INFO]  ${e.message}`;
    case "warn":
      return `[WARN]  ${e.message} (code ${e.code})`;
    case "error":
      return `[ERROR] ${e.message}: ${e.error.message}`;
    default:
      return assertNever(e);
  }
}

function severity(e: LogEntry): number {
  switch (e.level) {
    case "info":  return 0;
    case "warn":  return 1;
    case "error": return 2;
    default:      return assertNever(e);
  }
}

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
