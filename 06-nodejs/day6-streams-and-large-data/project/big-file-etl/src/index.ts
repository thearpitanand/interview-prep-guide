/**
 * index.ts — CLI entry point for the big-file ETL.
 *
 * Usage:
 *   npx tsx src/index.ts [input-path] [output-path]
 *
 * Defaults:
 *   input:  data/events.ndjson
 *   output: out/summary.csv
 *
 * Run the generator first:
 *   npx tsx data/generate.ts
 */

import { resolve } from "node:path";
import { existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { runPipeline } from "./pipeline.js";

const __dirname = fileURLToPath(new URL(".", import.meta.url));

// ---------------------------------------------------------------------------
// Argument parsing
// ---------------------------------------------------------------------------

const args = process.argv.slice(2);

const inputPath = resolve(
  __dirname,
  "..",
  args[0] ?? "data/events.ndjson"
);
const outputPath = resolve(
  __dirname,
  "..",
  args[1] ?? "out/summary.csv"
);

// ---------------------------------------------------------------------------
// Pre-flight checks
// ---------------------------------------------------------------------------

if (!existsSync(inputPath)) {
  console.error(`Input file not found: ${inputPath}`);
  console.error("Run the generator first:");
  console.error("  npx tsx data/generate.ts");
  process.exit(1);
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

console.log("=".repeat(60));
console.log("Big-File ETL — Streaming Pipeline");
console.log("=".repeat(60));
console.log(`Input:  ${inputPath}`);
console.log(`Output: ${outputPath}`);
console.log("");

let lastProgressRow = 0;

function onProgress(rowsRead: number): void {
  if (rowsRead > lastProgressRow) {
    process.stdout.write(`  Processed ${rowsRead.toLocaleString()} rows...\r`);
    lastProgressRow = rowsRead;
  }
}

try {
  const result = await runPipeline(inputPath, outputPath, onProgress);

  // Clear the progress line
  process.stdout.write(" ".repeat(60) + "\r");

  console.log("Pipeline complete.");
  console.log("");
  console.log("Results:");
  console.log(`  Rows read:           ${result.rowsRead.toLocaleString()}`);
  console.log(`  Rows valid:          ${result.rowsValid.toLocaleString()}`);
  console.log(`  Rows invalid (Zod):  ${result.rowsInvalid.toLocaleString()}`);
  console.log(`  Malformed JSON:      ${result.rowsMalformedJson.toLocaleString()}`);
  console.log(`  Categories found:    ${result.categoriesFound}`);
  console.log(`  Elapsed:             ${result.elapsedMs} ms`);
  console.log("");
  console.log("Category Summary:");
  console.log(
    "  " +
      ["Category".padEnd(14), "Events".padStart(8), "Total ($)".padStart(12), "Avg ($)".padStart(10), "Flagged".padStart(9)].join("  ")
  );
  console.log("  " + "-".repeat(60));

  for (const row of result.summary) {
    const totalDollars = (row.total_amount_cents / 100).toFixed(2);
    const avgDollars = (row.avg_amount_cents / 100).toFixed(2);
    console.log(
      "  " +
        [
          row.category.padEnd(14),
          row.event_count.toLocaleString().padStart(8),
          `$${totalDollars}`.padStart(12),
          `$${avgDollars}`.padStart(10),
          row.flagged_count.toLocaleString().padStart(9),
        ].join("  ")
    );
  }

  console.log("");
  console.log(`Output written to: ${outputPath}`);
} catch (err) {
  console.error("ETL pipeline failed:", err);
  process.exit(1);
}
