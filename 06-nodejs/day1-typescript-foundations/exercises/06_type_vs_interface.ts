/**
 * Day 1 — Exercise 06: type vs interface
 *
 * Define the same shape both ways, extend an interface, intersect a type,
 * show declaration merging, and practice the rule-of-thumb for choosing.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/06_type_vs_interface.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - interface TransactionInterface         — id: string, date: string, amount: number, category: string
//   - type TransactionType                   — same shape as TransactionInterface (using type syntax)
//   - function describeInterface(tx: TransactionInterface): string
//       — "<date> | <category> | <+/-><amount.toFixed(2)>"
//   - function describeType(tx: TransactionType): string
//       — same format as describeInterface
//   - const sampleTx                         — id "tx_001", date "2024-03-15", amount -52.30, category "groceries"
//   - interface BaseRecord                   — id: string, createdAt: string
//   - interface AnnotatedTransaction extends BaseRecord
//       — adds amount: number, category: string, note?: string
//   - function formatAnnotated(tx: AnnotatedTransaction): string
//       — "[<id>] <amount.toFixed(2)>" with optional " (<note>)" suffix
//   - type BaseRecordType                    — { id: string; createdAt: string }
//   - type AnnotatedTransactionType          — BaseRecordType & { amount: number; category: string; note?: string }
//   - function formatAnnotatedType(tx: AnnotatedTransactionType): string
//       — same format as formatAnnotated
//   - interface AppConfig (declared twice)   — first with host: string, then with port: number (declaration merging)
//   - const config: AppConfig               — host "localhost", port 3000
//   - type AppConfigV2                       — { host: string } & { port: number }
//   - const configV2: AppConfigV2           — host "localhost", port 3000
//   - type ID                               — string | number
//   - type StringPair                        — [string, string]
//   - function lookupById(id: ID): string   — if string return it, if number return String(id)
// Read the tests to infer expected values.

// ---------- TESTS ----------

// Both syntaxes accept the same shape
assert.equal(describeInterface(sampleTx), "2024-03-15 | groceries | -52.30");
assert.equal(describeType(sampleTx), "2024-03-15 | groceries | -52.30");

// Extended interface includes base fields
const annotated: AnnotatedTransaction = {
  id: "tx_002",
  createdAt: "2024-03-15T10:00:00Z",
  amount: 200.0,
  category: "income",
  note: "freelance payment",
};
assert.equal(formatAnnotated(annotated), "[tx_002] 200.00 (freelance payment)");

// Optional note absent
const annotatedNoNote: AnnotatedTransaction = {
  id: "tx_003",
  createdAt: "2024-03-16T09:00:00Z",
  amount: -30.0,
  category: "transport",
};
assert.equal(formatAnnotated(annotatedNoNote), "[tx_003] -30.00");

// Type intersection works the same way
const annotatedT: AnnotatedTransactionType = {
  id: "tx_004",
  createdAt: "2024-03-17T08:00:00Z",
  amount: -15.5,
  category: "utilities",
  note: "phone bill",
};
assert.equal(formatAnnotatedType(annotatedT), "[tx_004] -15.50 (phone bill)");

// Declaration-merged AppConfig has both fields
assert.equal(config.host, "localhost");
assert.equal(config.port, 3000);

// Type intersection version
assert.equal(configV2.host, "localhost");
assert.equal(configV2.port, 3000);

// Union type — lookupById
assert.equal(lookupById("abc-123"), "abc-123");
assert.equal(lookupById(42), "42");

// Tuple alias
const pair: StringPair = ["first", "second"];
assert.equal(pair[0], "first");
assert.equal(pair[1], "second");

console.log("All tests passed!");
