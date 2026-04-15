/**
 * Day 1 — Exercise 07: readonly and Immutability
 *
 * Use Readonly<T>, ReadonlyArray<T>, and as const to express immutability
 * constraints that the compiler can enforce at the call site.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/07_readonly_and_immutability.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - interface Transaction               — id: string, date: string, amount: number,
//                                           category: string, description: string
//   - type FrozenTransaction              — Readonly<Transaction>
//   - function formatTransaction(tx: FrozenTransaction): string
//       — "<date> | <category padEnd(12)> | <+/-><amount.toFixed(2)> | <description>"
//   - function totalIncome(transactions: ReadonlyArray<Transaction>): number
//       — sum of all amounts > 0
//   - function totalExpenses(transactions: ReadonlyArray<Transaction>): number
//       — sum of all amounts < 0
//   - function groupByCategory(transactions: ReadonlyArray<Transaction>): Record<string, Transaction[]>
//       — groups transactions by category without mutating input
//   - const CATEGORY_LABELS               — as const object mapping:
//       groceries → "Groceries", utilities → "Utilities", transport → "Transport",
//       dining → "Dining Out", income → "Income"
//   - type CategoryKey                    — keyof typeof CATEGORY_LABELS
//   - function getCategoryLabel(key: CategoryKey): string
//       — returns CATEGORY_LABELS[key]
//   - const EXPENSE_CATEGORIES            — as const array: ["groceries", "utilities", "transport", "dining"]
//   - type ExpenseCategory                — typeof EXPENSE_CATEGORIES[number]
//   - function isExpenseCategory(value: string): value is ExpenseCategory
//       — returns true if value is in EXPENSE_CATEGORIES
//   - const transactions: Transaction[]   — 6 entries (see test assertions for structure)
// Read the tests to infer expected values.

// ---------- TESTS ----------

// formatTransaction produces the expected string shape
const formatted = formatTransaction(transactions[0]!);
assert.ok(formatted.includes("2024-03-01"));
assert.ok(formatted.includes("income"));
assert.ok(formatted.includes("+1800.00"));
assert.ok(formatted.includes("Paycheck"));

// totalIncome sums only positive amounts
const income = totalIncome(transactions);
assert.ok(Math.abs(income - 2050.0) < 0.001);

// totalExpenses sums only negative amounts
const expenses = totalExpenses(transactions);
assert.ok(Math.abs(expenses - (-205.8)) < 0.001);

// groupByCategory splits correctly
const grouped = groupByCategory(transactions);
assert.equal(grouped["income"]?.length, 2);
assert.equal(grouped["groceries"]?.length, 1);
assert.equal(grouped["utilities"]?.length, 1);
assert.equal(grouped["transport"]?.length, 1);

// as const object — getCategoryLabel
assert.equal(getCategoryLabel("groceries"), "Groceries");
assert.equal(getCategoryLabel("dining"), "Dining Out");
assert.equal(getCategoryLabel("income"), "Income");

// as const array — isExpenseCategory type guard
assert.equal(isExpenseCategory("groceries"), true);
assert.equal(isExpenseCategory("transport"), true);
assert.equal(isExpenseCategory("income"), false);   // income is not an expense category
assert.equal(isExpenseCategory("unknown"), false);

// original array is unmodified after passing to readonly functions
assert.equal(transactions.length, 6);

console.log("All tests passed!");
