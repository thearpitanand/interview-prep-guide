/**
 * types.ts — Discriminated union for heterogeneous log entries.
 *
 * Each entry has a `kind` discriminant. Guards check every field so
 * parseLogLine can reject malformed lines at the boundary.
 */

// ── Discriminated union ────────────────────────────────────────────────────

export type RequestEntry = unknown; // TODO: define RequestEntry

export type DbQueryEntry = unknown; // TODO: define DbQueryEntry

export type CacheHitEntry = unknown; // TODO: define CacheHitEntry

export type ErrorEntry = unknown; // TODO: define ErrorEntry

export type MetricEntry = unknown; // TODO: define MetricEntry

export type LogEntry =
  | RequestEntry
  | DbQueryEntry
  | CacheHitEntry
  | ErrorEntry
  | MetricEntry; // TODO: define LogEntry as a discriminated union of the above

// ── assertNever for exhaustive switches ────────────────────────────────────

export function assertNever(x: never): never {
  throw new Error("TODO: implement assertNever");
}

// ── Per-kind type guards ───────────────────────────────────────────────────

// ── Top-level guard ────────────────────────────────────────────────────────

export function isLogEntry(x: unknown): x is LogEntry {
  throw new Error("TODO: implement isLogEntry");
}

// ── Line parser ───────────────────────────────────────────────────────────

export function parseLogLine(raw: string): LogEntry | null {
  throw new Error("TODO: implement parseLogLine");
}
