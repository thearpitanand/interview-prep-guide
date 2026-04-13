# Big-File ETL — Streaming Pipeline

A fully streaming ETL that reads a 100k-row NDJSON file, validates each row with Zod, aggregates by category with bounded memory, and writes a CSV summary.

## Run Commands

```bash
# Step 1: generate the input file (100,000 rows, ~12 MB)
npx tsx data/generate.ts

# Step 2: run the ETL pipeline
npx tsx src/index.ts

# Optional: generate 1 million rows instead
ROW_COUNT=1000000 npx tsx data/generate.ts
npx tsx src/index.ts
```

Both commands run from the `project/big-file-etl/` directory (or provide full paths).

## Files

```
big-file-etl/
├── src/
│   ├── schema.ts      Zod schema for EventRecord + CategorySummary types
│   ├── pipeline.ts    Streaming ETL: read → validate → aggregate → write CSV
│   └── index.ts       CLI entry point, prints timing and summary table
├── data/
│   ├── generate.ts    Generates events.ndjson (100k rows, seeded PRNG)
│   └── events.ndjson  (created by generate.ts, gitignored)
├── out/
│   ├── .gitkeep
│   └── summary.csv    (created by the pipeline)
└── README.md
```

## Memory Expectations

| Phase | Memory used |
|-------|-------------|
| Reading input | One line at a time (~few hundred bytes) |
| Aggregator Map | 20 entries max (one per category) |
| Output CSV | Streamed row-by-row via csv-stringify |
| Peak heap | Roughly constant regardless of file size |

The pipeline is designed to stay memory-flat. Heap usage does not grow with row count. Run with `--inspect` and observe the memory profile to verify.

## Acceptance Checklist

- [ ] `npx tsx data/generate.ts` completes and writes `data/events.ndjson`
- [ ] `npx tsx src/index.ts` reads the file and writes `out/summary.csv`
- [ ] `out/summary.csv` has exactly 20 rows (one per category) + 1 header
- [ ] All 100,000 rows are reported as "Rows valid" (no schema errors)
- [ ] Elapsed time is under 5 seconds for 100k rows on a modern machine
- [ ] Re-running the generator produces the same `events.ndjson` (deterministic seed)
- [ ] `ROW_COUNT=1000000 npx tsx data/generate.ts && npx tsx src/index.ts` stays under ~100 MB heap

## Schema

Each row in `events.ndjson`:

```json
{
  "id": 1,
  "ts": 1700042341,
  "category": "electronics",
  "userId": "3f4a1b2c-...",
  "amountCents": 4999,
  "quantity": 2,
  "flagged": false
}
```

Output `summary.csv` columns: `category`, `event_count`, `total_amount_cents`, `total_quantity`, `flagged_count`, `avg_amount_cents`.
