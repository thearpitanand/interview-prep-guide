/**
 * ledger-cli — Day 1 Project
 *
 * Reads data/sample.json and prints a formatted summary of income,
 * expenses, net balance, and spending by category.
 *
 * Run: npx tsx day1-typescript-foundations/project/ledger-cli/src/index.ts
 */
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { join, dirname } from "node:path";

// ---------- Types ----------

interface Transaction {
  id: string;
  date: string;
  description: string;
  amount: number;
  category: string;
}

// ---------- Load data ----------

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const dataPath = join(__dirname, "..", "data", "sample.json");

const raw = readFileSync(dataPath, "utf-8");
const transactions: Transaction[] = JSON.parse(raw) as Transaction[];

// ---------- Compute summary ----------

function computeSummary(txs: readonly Transaction[]): {
  totalIncome: number;
  totalExpenses: number;
  net: number;
  countByCategory: Record<string, number>;
  spendByCategory: Record<string, number>;
  transactionCount: number;
} {
  if (txs.length === 0) {
    return {
      totalIncome: 0,
      totalExpenses: 0,
      net: 0,
      countByCategory: {},
      spendByCategory: {},
      transactionCount: 0,
    };
  }

  let totalIncome = 0;
  let totalExpenses = 0;
  const countByCategory: Record<string, number> = {};
  const spendByCategory: Record<string, number> = {};

  for (const tx of txs) {
    if (tx.amount > 0) {
      totalIncome += tx.amount;
    } else {
      totalExpenses += tx.amount;
    }

    const prevCount = countByCategory[tx.category] ?? 0;
    countByCategory[tx.category] = prevCount + 1;

    const prevSpend = spendByCategory[tx.category] ?? 0;
    spendByCategory[tx.category] = prevSpend + tx.amount;
  }

  return {
    totalIncome,
    totalExpenses,
    net: totalIncome + totalExpenses,
    countByCategory,
    spendByCategory,
    transactionCount: txs.length,
  };
}

// ---------- Formatting helpers ----------

function pad(s: string, width: number, right = false): string {
  if (right) return s.padStart(width);
  return s.padEnd(width);
}

function fmtAmount(n: number): string {
  const sign = n >= 0 ? "+" : "-";
  return `${sign}$${Math.abs(n).toFixed(2)}`;
}

function separator(char = "-", width = 52): string {
  return char.repeat(width);
}

// Top N categories by absolute spend (expenses only, most negative first)
function topCategories(
  spendByCategory: Record<string, number>,
  n: number
): Array<[string, number]> {
  return Object.entries(spendByCategory)
    .filter(([, amount]) => amount < 0)
    .sort(([, a], [, b]) => a - b)      // most negative first
    .slice(0, n);
}

// ---------- Print summary ----------

const summary = computeSummary(transactions);

console.log(separator("="));
console.log("  LEDGER SUMMARY");
console.log(separator("="));
console.log(`  Transactions : ${summary.transactionCount}`);
console.log(`  Total income : ${pad(fmtAmount(summary.totalIncome), 12, true)}`);
console.log(`  Total expenses: ${pad(fmtAmount(summary.totalExpenses), 12, true)}`);
console.log(`  Net balance  : ${pad(fmtAmount(summary.net), 12, true)}`);
console.log(separator());

console.log("  TRANSACTIONS BY CATEGORY");
console.log(separator());
console.log(
  `  ${"Category".padEnd(14)} ${"Count".padStart(5)}  ${"Spend".padStart(12)}`
);
console.log(separator());

const categoryEntries = Object.entries(summary.countByCategory).sort(([a], [b]) =>
  a.localeCompare(b)
);

for (const [cat, count] of categoryEntries) {
  const spend = summary.spendByCategory[cat] ?? 0;
  console.log(
    `  ${pad(cat, 14)} ${String(count).padStart(5)}  ${pad(fmtAmount(spend), 12, true)}`
  );
}

console.log(separator());
console.log("  TOP 3 EXPENSE CATEGORIES");
console.log(separator());

const top3 = topCategories(summary.spendByCategory, 3);

if (top3.length === 0) {
  console.log("  No expense categories found.");
} else {
  for (let i = 0; i < top3.length; i++) {
    const entry = top3[i];
    if (entry === undefined) continue;
    const [cat, spend] = entry;
    console.log(`  ${i + 1}. ${pad(cat, 12)} ${pad(fmtAmount(spend), 12, true)}`);
  }
}

console.log(separator("="));
