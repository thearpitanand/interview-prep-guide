/**
 * index.ts — CLI entry point for the config-and-api-loader project.
 *
 * Reads data/config.json, data/users.json, and data/api_response.json,
 * validates each with Zod, and prints a readable summary including
 * per-field error messages for every invalid record.
 *
 * Run: npx tsx day5-runtime-validation-zod/project/config-and-api-loader/src/index.ts
 */
import { z } from "zod";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { loadConfig, loadUsers, loadApiResponse } from "./load.ts";

// Resolve paths relative to this file so the script works from any cwd
const __dir = dirname(fileURLToPath(import.meta.url));
const dataDir = join(__dir, "..", "data");

async function main(): Promise<void> {
  throw new Error("TODO: implement CLI entry point");
}

main().catch((err: unknown) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
