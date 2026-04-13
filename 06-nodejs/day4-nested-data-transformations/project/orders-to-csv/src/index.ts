/**
 * orders-to-csv — Day 4 Project
 *
 * Reads data/customers.json and produces:
 *   out/line_items.csv     — one row per line item
 *   out/customer_totals.csv — one row per customer with aggregated stats
 *
 * Run:
 *   npx tsx day4-nested-data-transformations/project/orders-to-csv/src/index.ts
 */

import { readFileSync, mkdirSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import {
  denormalize,
  aggregateCustomers,
  toCSV,
  type Customer,
} from "./transforms.js";

// ---------------------------------------------------------------------------
// Resolve paths relative to this file (ESM-safe)
// ---------------------------------------------------------------------------

const __filename = fileURLToPath(import.meta.url);
const __dir      = dirname(__filename);
const projectRoot = join(__dir, "..");

const dataDir = join(projectRoot, "data");
const outDir  = join(projectRoot, "out");

// ---------------------------------------------------------------------------
// 1. Read and parse customers.json
// ---------------------------------------------------------------------------

const rawJson = readFileSync(join(dataDir, "customers.json"), "utf-8");
const parsed  = JSON.parse(rawJson) as { customers: Customer[] };
const customers: Customer[] = parsed.customers;

console.log(`Loaded ${customers.length} customers from customers.json`);

// ---------------------------------------------------------------------------
// 2. Denormalize: customer → order → item → flat row
// ---------------------------------------------------------------------------

const lineItems = denormalize(customers);
console.log(`Denormalized to ${lineItems.length} line-item rows`);

// ---------------------------------------------------------------------------
// 3. Aggregate: per-customer totals
// ---------------------------------------------------------------------------

const customerTotals = aggregateCustomers(lineItems, customers);

// ---------------------------------------------------------------------------
// 4. Ensure out/ directory exists
// ---------------------------------------------------------------------------

mkdirSync(outDir, { recursive: true });

// ---------------------------------------------------------------------------
// 5. Write line_items.csv
// ---------------------------------------------------------------------------

const lineItemsPath = join(outDir, "line_items.csv");
// toCSV requires Record<string, unknown>[] — cast through the compatible shape
const lineItemCSV = toCSV(lineItems as unknown as Record<string, unknown>[]);
writeFileSync(lineItemsPath, lineItemCSV, "utf-8");
console.log(`Wrote ${lineItems.length} rows → out/line_items.csv`);

// ---------------------------------------------------------------------------
// 6. Write customer_totals.csv
// ---------------------------------------------------------------------------

const totalsPath = join(outDir, "customer_totals.csv");
const totalsCSV  = toCSV(customerTotals as unknown as Record<string, unknown>[]);
writeFileSync(totalsPath, totalsCSV, "utf-8");
console.log(`Wrote ${customerTotals.length} rows → out/customer_totals.csv`);

// ---------------------------------------------------------------------------
// 7. Print summary to stdout
// ---------------------------------------------------------------------------

const grandTotal = customerTotals.reduce((sum, c) => sum + c.totalSpend, 0);
const totalOrders = customerTotals.reduce((sum, c) => sum + c.orderCount, 0);

console.log("\n=== Summary ===");
console.log(`Customers  : ${customers.length}`);
console.log(`Orders     : ${totalOrders}`);
console.log(`Line items : ${lineItems.length}`);
console.log(`Grand total: $${(Math.round(grandTotal * 100) / 100).toFixed(2)}`);
console.log("\nTop customers by spend:");

const sorted = [...customerTotals].sort((a, b) => b.totalSpend - a.totalSpend);
for (const c of sorted.slice(0, 5)) {
  console.log(
    `  ${c.name.padEnd(16)} (${c.tier.padEnd(6)})  ` +
    `$${c.totalSpend.toFixed(2).padStart(8)}  ` +
    `${c.orderCount} order(s), ${c.itemCount} item(s)`
  );
}
