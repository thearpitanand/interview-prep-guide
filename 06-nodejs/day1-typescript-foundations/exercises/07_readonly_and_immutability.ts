/**
 * Day 1 — Exercise 07: readonly and Immutability
 *
 * Use Readonly<T>, ReadonlyArray<T>, and as const to express immutability
 * constraints that the compiler can enforce at the call site.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/07_readonly_and_immutability.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

interface Transaction {
  id: string;
  date: string;
  amount: number;
  category: string;
  description: string;
}

// Readonly<T> makes every property readonly — useful for "frozen" records
type FrozenTransaction = Readonly<Transaction>;

// A function that accepts a frozen transaction and computes a display string
function formatTransaction(tx: FrozenTransaction): string {
  const sign = tx.amount >= 0 ? "+" : "";
  return `${tx.date} | ${tx.category.padEnd(12)} | ${sign}${tx.amount.toFixed(2)} | ${tx.description}`;
}

// --- ReadonlyArray<T> / readonly T[] ---

// This function promises not to mutate the input array.
// The caller's array is never at risk.
function totalIncome(transactions: ReadonlyArray<Transaction>): number {
  return transactions
    .filter((tx) => tx.amount > 0)
    .reduce((acc, tx) => acc + tx.amount, 0);
}

function totalExpenses(transactions: ReadonlyArray<Transaction>): number {
  return transactions
    .filter((tx) => tx.amount < 0)
    .reduce((acc, tx) => acc + tx.amount, 0);
}

// A function that groups transactions by category without mutating the input
function groupByCategory(
  transactions: ReadonlyArray<Transaction>
): Record<string, Transaction[]> {
  const result: Record<string, Transaction[]> = {};
  for (const tx of transactions) {
    const existing = result[tx.category];
    if (existing !== undefined) {
      existing.push(tx);
    } else {
      result[tx.category] = [tx];
    }
  }
  return result;
}

// --- as const for configuration / lookup tables ---

const CATEGORY_LABELS = {
  groceries: "Groceries",
  utilities: "Utilities",
  transport: "Transport",
  dining: "Dining Out",
  income: "Income",
} as const;

// typeof CATEGORY_LABELS gives the readonly literal object type
type CategoryKey = keyof typeof CATEGORY_LABELS;

function getCategoryLabel(key: CategoryKey): string {
  return CATEGORY_LABELS[key];
}

// as const array — derives a union type from array elements
const EXPENSE_CATEGORIES = ["groceries", "utilities", "transport", "dining"] as const;
type ExpenseCategory = typeof EXPENSE_CATEGORIES[number];

function isExpenseCategory(value: string): value is ExpenseCategory {
  // The cast to readonly string[] is needed to use includes on the const array
  return (EXPENSE_CATEGORIES as readonly string[]).includes(value);
}

// --- Demonstrate what readonly prevents (compile error shown in comment) ---
//
// If you tried to write:
//   function badMutator(tx: FrozenTransaction): void {
//     tx.amount = 999;  // ERROR: Cannot assign to 'amount' because it is a read-only property.
//   }
//
// TypeScript catches this at compile time. The value is safe from accidental mutation.

// Similarly, with ReadonlyArray:
//   function badArrayMutator(txs: ReadonlyArray<Transaction>): void {
//     txs.push({ ... });  // ERROR: Property 'push' does not exist on type 'readonly Transaction[]'
//   }

// Sample data
const transactions: Transaction[] = [
  { id: "tx_001", date: "2024-03-01", amount: 1800.0,  category: "income",    description: "Paycheck" },
  { id: "tx_002", date: "2024-03-02", amount: -52.30,  category: "groceries", description: "Weekly shop" },
  { id: "tx_003", date: "2024-03-03", amount: -110.0,  category: "utilities", description: "Electric bill" },
  { id: "tx_004", date: "2024-03-05", amount: -28.50,  category: "dining",    description: "Dinner with team" },
  { id: "tx_005", date: "2024-03-08", amount: 250.0,   category: "income",    description: "Freelance project" },
  { id: "tx_006", date: "2024-03-10", amount: -15.0,   category: "transport", description: "Bus pass" },
];

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
