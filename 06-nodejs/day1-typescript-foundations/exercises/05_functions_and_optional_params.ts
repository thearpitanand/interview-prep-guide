/**
 * Day 1 — Exercise 05: Functions and Optional Parameters
 *
 * Demonstrate optional parameters, default values, rest parameters, typed
 * callbacks, and higher-order functions with explicit function type signatures.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/05_functions_and_optional_params.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - function formatUserLine(email: string, displayName?: string): string
//       — with displayName: "<displayName> <<email>>"
//       — without: just email
//   - function createLabel(text: string, prefix = "INFO"): string
//       — returns "[<prefix>] <text>"
//   - function buildRecord(id: string, amount: number, ...tags: string[]): string
//       — no tags: "<id>: <amount.toFixed(2)>"
//       — with tags: "<id>: <amount.toFixed(2)> [<tag1>, <tag2>]"
//   - type NumberFormatter                   — (value: number, decimals: number) => string
//   - const formatFixed: NumberFormatter     — returns value.toFixed(decimals)
//   - const formatPercent: NumberFormatter   — returns "<value*100.toFixed(decimals)>%"
//   - function transformAmounts(amounts: readonly number[], transform: (n: number) => number): number[]
//       — applies transform to each element (use .map)
//   - function makeFilter(predicate: (n: number) => boolean): (values: number[]) => number[]
//       — returns a function that filters an array by predicate
//   - const keepPositive                     — makeFilter result for n > 0
//   - const keepNegative                     — makeFilter result for n < 0
//   - type TransactionLine                   — { description: string; amount: number }
//   - function processLines(lines: readonly TransactionLine[], onLine: (line: TransactionLine, index: number) => string): string[]
//       — maps each line through onLine callback
//   - const sampleLines: TransactionLine[]   — 3 entries: see test assertions for values
//   - const formatted                        — processLines result with index+1 prefix formatting
// Read the tests to infer expected values.

// ---------- TESTS ----------

// optional param — with displayName
assert.equal(formatUserLine("a@b.com", "Alice"), "Alice <a@b.com>");

// optional param — without displayName
assert.equal(formatUserLine("b@c.com"), "b@c.com");

// default param — uses default when omitted
assert.equal(createLabel("file parsed"), "[INFO] file parsed");

// default param — explicit override
assert.equal(createLabel("disk full", "WARN"), "[WARN] disk full");

// rest params — no tags
assert.equal(buildRecord("tx_001", 42.5), "tx_001: 42.50");

// rest params — multiple tags
assert.equal(buildRecord("tx_002", -15.0, "reviewed", "flagged"), "tx_002: -15.00 [reviewed, flagged]");

// function type alias — formatFixed
assert.equal(formatFixed(3.14159, 2), "3.14");

// function type alias — formatPercent
assert.equal(formatPercent(0.125, 1), "12.5%");

// higher-order: transformAmounts
const doubled = transformAmounts([10, -20, 30], (n) => n * 2);
assert.deepEqual(doubled, [20, -40, 60]);

// higher-order: makeFilter
const mixed = [100, -50, 200, -75, 0];
assert.deepEqual(keepPositive(mixed), [100, 200]);
assert.deepEqual(keepNegative(mixed), [-50, -75]);

// callback-based processLines
assert.equal(formatted[0], "1. Grocery run: -52.30");
assert.equal(formatted[1], "2. Paycheck: +1800.00");
assert.equal(formatted[2], "3. Electric bill: -110.00");

console.log("All tests passed!");
