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

// ---------- ERROR FORMATTING ----------

function formatFieldErrors(error: z.ZodError): string {
  const flat = error.flatten();
  const lines: string[] = [];

  if (flat.formErrors.length > 0) {
    lines.push(`  (form): ${flat.formErrors.join(", ")}`);
  }

  for (const [field, msgs] of Object.entries(flat.fieldErrors)) {
    if (msgs && msgs.length > 0) {
      lines.push(`  ${field}: ${msgs.join(", ")}`);
    }
  }

  // Also surface nested errors that flatten() misses (paths > 1 level deep)
  const nestedPaths = new Set(lines.map((l) => l.trim().split(":")[0]));
  for (const issue of error.issues) {
    if (issue.path.length > 1) {
      const key = issue.path.join(".");
      if (!nestedPaths.has(key)) {
        lines.push(`  ${key}: ${issue.message}`);
        nestedPaths.add(key);
      }
    }
  }

  return lines.join("\n") || "  (unknown validation error)";
}

// ---------- SECTION PRINTERS ----------

function printSeparator(title: string): void {
  console.log(`\n${"=".repeat(50)}`);
  console.log(`  ${title}`);
  console.log("=".repeat(50));
}

// ---------- MAIN ----------

async function main(): Promise<void> {
  let totalValid = 0;
  let totalInvalid = 0;

  // --- Config ---
  printSeparator("Config");
  const configResult = await loadConfig(join(dataDir, "config.json"));
  totalValid += configResult.valid.length;
  totalInvalid += configResult.invalid.length;

  console.log(
    `Loaded: ${configResult.valid.length} valid, ${configResult.invalid.length} invalid`
  );

  if (configResult.valid.length > 0 && configResult.valid[0] !== undefined) {
    const cfg = configResult.valid[0];
    console.log(`  App:         ${cfg.app.name} v${cfg.app.version} (${cfg.app.environment})`);
    console.log(`  Server:      ${cfg.server.host}:${cfg.server.port}`);
    console.log(`  Database:    ${cfg.database.host}:${cfg.database.port}/${cfg.database.name}`);
    console.log(`  Log level:   ${cfg.logging.level}`);
  }

  for (let i = 0; i < configResult.invalid.length; i++) {
    const inv = configResult.invalid[i];
    if (inv !== undefined) {
      console.log(`\nInvalid config:\n${formatFieldErrors(inv.error)}`);
    }
  }

  // --- Users ---
  printSeparator("Users");
  const usersResult = await loadUsers(join(dataDir, "users.json"));
  totalValid += usersResult.valid.length;
  totalInvalid += usersResult.invalid.length;

  console.log(
    `Loaded: ${usersResult.valid.length} valid, ${usersResult.invalid.length} invalid`
  );

  if (usersResult.valid.length > 0) {
    console.log("\nValid users:");
    for (const u of usersResult.valid) {
      console.log(`  [${u.role.padEnd(9)}] ${u.name} <${u.email}>`);
    }
  }

  if (usersResult.invalid.length > 0) {
    console.log("\nInvalid records:");
    for (let i = 0; i < usersResult.invalid.length; i++) {
      const inv = usersResult.invalid[i];
      if (inv !== undefined) {
        const raw = inv.raw as Record<string, unknown>;
        const label = typeof raw["email"] === "string"
          ? raw["email"]
          : typeof raw["name"] === "string"
          ? raw["name"]
          : `record #${i + 1}`;
        console.log(`\n  [invalid] ${label}`);
        console.log(formatFieldErrors(inv.error));
      }
    }
  }

  // --- API Response ---
  printSeparator("API Response");
  const apiResult = await loadApiResponse(join(dataDir, "api_response.json"));
  totalValid += apiResult.valid.length;
  totalInvalid += apiResult.invalid.length;

  console.log(
    `Loaded: ${apiResult.valid.length} valid, ${apiResult.invalid.length} invalid`
  );

  if (apiResult.valid.length > 0 && apiResult.valid[0] !== undefined) {
    const resp = apiResult.valid[0];
    console.log(`  Status:     ${resp.status}`);
    console.log(`  Request ID: ${resp.requestId}`);

    if (resp.status === "success") {
      console.log(`  Results:    ${resp.results.length} records`);
      for (const r of resp.results) {
        console.log(
          `    [${r.type.padEnd(11)}] ${r.id}  ${r.currency} ${r.amount.toFixed(2).padStart(10)}  — ${r.description}`
        );
      }
      console.log(`  Total declared: ${resp.meta.total}`);
    } else {
      console.log(`  Error code: ${resp.code}`);
      console.log(`  Message:    ${resp.message}`);
    }
  }

  for (let i = 0; i < apiResult.invalid.length; i++) {
    const inv = apiResult.invalid[i];
    if (inv !== undefined) {
      console.log(`\nInvalid API response:\n${formatFieldErrors(inv.error)}`);
    }
  }

  // --- Summary ---
  printSeparator("Summary");
  console.log(`  Total valid:   ${totalValid}`);
  console.log(`  Total invalid: ${totalInvalid}`);
  console.log("");
}

main().catch((err: unknown) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
