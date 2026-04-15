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
// main
// ---------------------------------------------------------------------------

function main(): void {
  throw new Error("TODO: implement CLI entry point");
}

main();
