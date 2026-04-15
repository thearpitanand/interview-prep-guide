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

async function main(): Promise<void> {
  throw new Error("TODO: implement CLI entry point");
}

main().catch((err: unknown) => {
  console.error("ETL pipeline failed:", err);
  process.exit(1);
});
