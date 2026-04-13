# Day 3 Project — Log Parser

## Run

```bash
npx tsx day3-advanced-types-for-data/project/log-parser/src/index.ts
```

## What It Does

Reads `data/logs.ndjson` — a Newline Delimited JSON file where each line is a JSON
object representing one log entry. Parses each line into a typed discriminated union,
rejects malformed lines gracefully, groups valid entries by `kind`, and prints a
summary table.

## Log Entry Kinds

| kind | Key Fields |
|---|---|
| `request` | `method`, `path`, `statusCode`, `durationMs` |
| `db_query` | `query`, `durationMs`, `rowCount` |
| `cache_hit` | `key`, `ttlMs` |
| `error` | `message`, `stack?` |
| `metric` | `name`, `value`, `unit` |

## Expected Output

```
=== Log Summary ===

Kind        Count   Notes
--------------------------------------------------
request     12      avg 120.4ms, 2 error responses
db_query    8       avg 20.8ms
cache_hit   6
error       4       first: "User not found"
metric      6
--------------------------------------------------
TOTAL       36      (3 line(s) rejected as invalid)
```

(Exact numbers depend on the log file contents.)

## Acceptance Checklist

- [ ] `src/types.ts` defines all 5 `kind` variants as a discriminated union
- [ ] `isLogEntry` guard checks every field, not just the `kind` string
- [ ] `parseLogLine` returns `null` for non-JSON lines and structurally invalid objects
- [ ] `src/index.ts` uses an exhaustive `switch` with `assertNever` as the default
- [ ] No `any` anywhere in the source
- [ ] The 3 intentionally malformed lines in `data/logs.ndjson` are rejected and counted
- [ ] Summary table prints per-kind count with relevant aggregate notes

## What You Are Practising

This project intentionally has no Zod. You write all validation by hand using the
type guards from `src/types.ts`. The point is to feel the cost of manual guards and
understand exactly what Zod automates (covered on Day 5).
