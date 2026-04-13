/**
 * types.ts — Discriminated union for heterogeneous log entries.
 *
 * Each entry has a `kind` discriminant. Guards check every field so
 * parseLogLine can reject malformed lines at the boundary.
 */

// ── Discriminated union ────────────────────────────────────────────────────

export type RequestEntry = {
  kind: "request";
  method: string;
  path: string;
  statusCode: number;
  durationMs: number;
};

export type DbQueryEntry = {
  kind: "db_query";
  query: string;
  durationMs: number;
  rowCount: number;
};

export type CacheHitEntry = {
  kind: "cache_hit";
  key: string;
  ttlMs: number;
};

export type ErrorEntry = {
  kind: "error";
  message: string;
  stack?: string;
};

export type MetricEntry = {
  kind: "metric";
  name: string;
  value: number;
  unit: string;
};

export type LogEntry =
  | RequestEntry
  | DbQueryEntry
  | CacheHitEntry
  | ErrorEntry
  | MetricEntry;

// ── assertNever for exhaustive switches ────────────────────────────────────

export function assertNever(x: never): never {
  throw new Error(`Unhandled log entry kind: ${JSON.stringify(x)}`);
}

// ── Per-kind type guards ───────────────────────────────────────────────────

function isRequestEntry(obj: Record<string, unknown>): obj is RequestEntry {
  return (
    typeof obj["method"]     === "string" &&
    typeof obj["path"]       === "string" &&
    typeof obj["statusCode"] === "number" &&
    typeof obj["durationMs"] === "number"
  );
}

function isDbQueryEntry(obj: Record<string, unknown>): obj is DbQueryEntry {
  return (
    typeof obj["query"]     === "string" &&
    typeof obj["durationMs"] === "number" &&
    typeof obj["rowCount"]   === "number"
  );
}

function isCacheHitEntry(obj: Record<string, unknown>): obj is CacheHitEntry {
  return (
    typeof obj["key"]   === "string" &&
    typeof obj["ttlMs"] === "number"
  );
}

function isErrorEntry(obj: Record<string, unknown>): obj is ErrorEntry {
  return (
    typeof obj["message"] === "string" &&
    (obj["stack"] === undefined || typeof obj["stack"] === "string")
  );
}

function isMetricEntry(obj: Record<string, unknown>): obj is MetricEntry {
  return (
    typeof obj["name"]  === "string" &&
    typeof obj["value"] === "number" &&
    typeof obj["unit"]  === "string"
  );
}

// ── Top-level guard ────────────────────────────────────────────────────────

export function isLogEntry(x: unknown): x is LogEntry {
  if (typeof x !== "object" || x === null) return false;
  const obj = x as Record<string, unknown>;
  const kind = obj["kind"];

  switch (kind) {
    case "request":   return isRequestEntry(obj);
    case "db_query":  return isDbQueryEntry(obj);
    case "cache_hit": return isCacheHitEntry(obj);
    case "error":     return isErrorEntry(obj);
    case "metric":    return isMetricEntry(obj);
    default:          return false;
  }
}

// ── Line parser ───────────────────────────────────────────────────────────

export function parseLogLine(raw: string): LogEntry | null {
  const trimmed = raw.trim();
  if (trimmed === "") return null;
  try {
    const parsed: unknown = JSON.parse(trimmed);
    return isLogEntry(parsed) ? parsed : null;
  } catch {
    return null;
  }
}
