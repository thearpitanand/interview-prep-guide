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
  /* TODO: define Transaction */
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
  throw new Error("TODO: implement computeSummary");
}

// ---------- Formatting helpers ----------

function pad(s: string, width: number, right = false): string {
  throw new Error("TODO: implement pad");
}

function fmtAmount(n: number): string {
  throw new Error("TODO: implement fmtAmount");
}

function separator(char = "-", width = 52): string {
  throw new Error("TODO: implement separator");
}

// Top N categories by absolute spend (expenses only, most negative first)
function topCategories(
  spendByCategory: Record<string, number>,
  n: number
): Array<[string, number]> {
  throw new Error("TODO: implement topCategories");
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
