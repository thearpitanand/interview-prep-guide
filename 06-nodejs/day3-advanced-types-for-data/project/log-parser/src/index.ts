/**
 * log-parser/src/index.ts
 *
 * Reads data/logs.ndjson, parses each line into a typed LogEntry,
 * groups by kind, and prints a summary table.
 *
 * Run: npx tsx day3-advanced-types-for-data/project/log-parser/src/index.ts
 */

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { join, dirname } from "node:path";
import {
  type LogEntry,
  type RequestEntry,
  type DbQueryEntry,
  type MetricEntry,
  parseLogLine,
  assertNever,
} from "./types.js";

// ── Resolve path relative to this file ────────────────────────────────────

const __filename = fileURLToPath(import.meta.url);
const __dir = dirname(__filename);
const dataPath = join(__dir, "../data/logs.ndjson");

// ── Read and parse ─────────────────────────────────────────────────────────

const raw = readFileSync(dataPath, "utf-8");
const lines = raw.split("\n");

let rejected = 0;
const entries: LogEntry[] = [];

for (const line of lines) {
  const entry = parseLogLine(line);
  if (entry === null) {
    if (line.trim() !== "") rejected++;
  } else {
    entries.push(entry);
  }
}

// ── Group by kind ──────────────────────────────────────────────────────────

type KindGroups = {
  request:   RequestEntry[];
  db_query:  DbQueryEntry[];
  cache_hit: LogEntry[];
  error:     LogEntry[];
  metric:    MetricEntry[];
};

const groups: KindGroups = {
  request:   [],
  db_query:  [],
  cache_hit: [],
  error:     [],
  metric:    [],
};

for (const entry of entries) {
  switch (entry.kind) {
    case "request":   groups.request.push(entry);   break;
    case "db_query":  groups.db_query.push(entry);  break;
    case "cache_hit": groups.cache_hit.push(entry); break;
    case "error":     groups.error.push(entry);     break;
    case "metric":    groups.metric.push(entry);    break;
    default:          assertNever(entry);
  }
}

// ── Summary helpers ────────────────────────────────────────────────────────

function avg(nums: number[]): number {
  if (nums.length === 0) return 0;
  return nums.reduce((a, b) => a + b, 0) / nums.length;
}

function col(s: string, width: number): string {
  return s.padEnd(width).slice(0, width);
}

// ── Print summary table ────────────────────────────────────────────────────

console.log("\n=== Log Summary ===\n");
console.log(
  col("Kind", 12) +
  col("Count", 8) +
  "Notes"
);
console.log("-".repeat(50));

// request
const reqDurations = groups.request.map((r) => r.durationMs);
const avgReqMs = avg(reqDurations).toFixed(1);
const errorReqs = groups.request.filter((r) => r.statusCode >= 400).length;
console.log(
  col("request", 12) +
  col(String(groups.request.length), 8) +
  `avg ${avgReqMs}ms, ${errorReqs} error responses`
);

// db_query
const dbDurations = groups.db_query.map((q) => q.durationMs);
const avgDbMs = avg(dbDurations).toFixed(1);
console.log(
  col("db_query", 12) +
  col(String(groups.db_query.length), 8) +
  `avg ${avgDbMs}ms`
);

// cache_hit
console.log(
  col("cache_hit", 12) +
  col(String(groups.cache_hit.length), 8) +
  ``
);

// error
console.log(
  col("error", 12) +
  col(String(groups.error.length), 8) +
  (groups.error.length > 0 ? `first: "${groups.error[0]?.kind === "error" ? (groups.error[0] as {kind:"error";message:string}).message : ""}"` : "none")
);

// metric
console.log(
  col("metric", 12) +
  col(String(groups.metric.length), 8) +
  ``
);

console.log("-".repeat(50));
console.log(
  col("TOTAL", 12) +
  col(String(entries.length), 8) +
  `(${rejected} line(s) rejected as invalid)`
);
console.log();
