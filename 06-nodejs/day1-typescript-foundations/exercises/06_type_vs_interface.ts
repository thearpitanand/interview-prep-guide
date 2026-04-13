/**
 * Day 1 — Exercise 06: type vs interface
 *
 * Define the same shape both ways, extend an interface, intersect a type,
 * show declaration merging, and practice the rule-of-thumb for choosing.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/06_type_vs_interface.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

// --- Same shape, two syntaxes ---

interface TransactionInterface {
  id: string;
  date: string;
  amount: number;
  category: string;
}

type TransactionType = {
  id: string;
  date: string;
  amount: number;
  category: string;
};

// Both accept the same object literal — they are structurally identical
function describeInterface(tx: TransactionInterface): string {
  return `${tx.date} | ${tx.category} | ${tx.amount >= 0 ? "+" : ""}${tx.amount.toFixed(2)}`;
}

function describeType(tx: TransactionType): string {
  return `${tx.date} | ${tx.category} | ${tx.amount >= 0 ? "+" : ""}${tx.amount.toFixed(2)}`;
}

// A value that satisfies both (structural typing — shape is what matters)
const sampleTx = {
  id: "tx_001",
  date: "2024-03-15",
  amount: -52.30,
  category: "groceries",
};

// --- Extending an interface ---

interface BaseRecord {
  id: string;
  createdAt: string;
}

// extends adds fields from the parent
interface AnnotatedTransaction extends BaseRecord {
  amount: number;
  category: string;
  note?: string;
}

function formatAnnotated(tx: AnnotatedTransaction): string {
  const note = tx.note ? ` (${tx.note})` : "";
  return `[${tx.id}] ${tx.amount.toFixed(2)}${note}`;
}

// --- Intersecting a type ---

type BaseRecordType = {
  id: string;
  createdAt: string;
};

// & merges both shapes into one
type AnnotatedTransactionType = BaseRecordType & {
  amount: number;
  category: string;
  note?: string;
};

function formatAnnotatedType(tx: AnnotatedTransactionType): string {
  const note = tx.note ? ` (${tx.note})` : "";
  return `[${tx.id}] ${tx.amount.toFixed(2)}${note}`;
}

// --- Declaration merging (interface only) ---
// Two interface declarations with the same name are merged automatically.
// This is useful for augmenting types from external libraries.

interface AppConfig {
  host: string;
}

interface AppConfig {
  port: number;
}

// AppConfig now has both host and port
const config: AppConfig = {
  host: "localhost",
  port: 3000,
};

// type cannot be redeclared — the equivalent for type is a new intersection
type AppConfigV2 = { host: string } & { port: number };

const configV2: AppConfigV2 = { host: "localhost", port: 3000 };

// --- When to prefer type ---
// type is required for unions, intersections of non-object types, and primitives

type ID = string | number;             // union — only type can do this
type StringPair = [string, string];    // tuple alias

function lookupById(id: ID): string {
  return typeof id === "string" ? id : String(id);
}

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
