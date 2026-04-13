/**
 * Day 1 — Exercise 05: Functions and Optional Parameters
 *
 * Demonstrate optional parameters, default values, rest parameters, typed
 * callbacks, and higher-order functions with explicit function type signatures.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/05_functions_and_optional_params.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

// Optional parameter — title is string | undefined inside the function body
function formatUserLine(email: string, displayName?: string): string {
  if (displayName !== undefined) {
    return `${displayName} <${email}>`;
  }
  return email;
}

// Default parameter — role is always string inside the body (never undefined)
function createLabel(text: string, prefix = "INFO"): string {
  return `[${prefix}] ${text}`;
}

// Rest parameter — accepts any number of additional tag strings
function buildRecord(id: string, amount: number, ...tags: string[]): string {
  const tagStr = tags.length > 0 ? ` [${tags.join(", ")}]` : "";
  return `${id}: ${amount.toFixed(2)}${tagStr}`;
}

// --- function types ---

// A named function type alias
type NumberFormatter = (value: number, decimals: number) => string;

// A function that matches the NumberFormatter signature
const formatFixed: NumberFormatter = (value, decimals) =>
  value.toFixed(decimals);

const formatPercent: NumberFormatter = (value, decimals) =>
  `${(value * 100).toFixed(decimals)}%`;

// --- higher-order functions ---

// Takes a list of values and a transform function; returns transformed values
function transformAmounts(
  amounts: readonly number[],
  transform: (n: number) => number
): number[] {
  return amounts.map(transform);
}

// Takes a predicate and returns a filter function (returns a function)
function makeFilter(predicate: (n: number) => boolean): (values: number[]) => number[] {
  return (values) => values.filter(predicate);
}

const keepPositive = makeFilter((n) => n > 0);
const keepNegative = makeFilter((n) => n < 0);

// A callback-accepting function that processes each transaction line
type TransactionLine = { description: string; amount: number };

function processLines(
  lines: readonly TransactionLine[],
  onLine: (line: TransactionLine, index: number) => string
): string[] {
  return lines.map((line, i) => onLine(line, i));
}

const sampleLines: TransactionLine[] = [
  { description: "Grocery run", amount: -52.30 },
  { description: "Paycheck", amount: 1800.00 },
  { description: "Electric bill", amount: -110.00 },
];

const formatted = processLines(sampleLines, (line, idx) =>
  `${idx + 1}. ${line.description}: ${line.amount >= 0 ? "+" : ""}${line.amount.toFixed(2)}`
);

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
