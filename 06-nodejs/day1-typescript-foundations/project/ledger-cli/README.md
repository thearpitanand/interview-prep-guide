# ledger-cli — Day 1 Project

A typed Node CLI that reads a JSON ledger file and prints a summary table of income, expenses, and spending by category.

Run: `npx tsx day1-typescript-foundations/project/ledger-cli/src/index.ts`

---

## Input shape

The CLI reads `data/sample.json`, which is an array of transaction objects:

```json
[
  {
    "id": "tx_001",
    "date": "2024-03-01",
    "description": "Monthly salary",
    "amount": 4200.0,
    "category": "income"
  }
]
```

| Field         | Type     | Notes                                         |
| ------------- | -------- | --------------------------------------------- |
| `id`          | `string` | Unique transaction identifier                 |
| `date`        | `string` | ISO 8601 date (`YYYY-MM-DD`)                  |
| `description` | `string` | Human-readable label                          |
| `amount`      | `number` | Positive = income, negative = expense         |
| `category`    | `string` | e.g. `"groceries"`, `"income"`, `"utilities"` |

---

## Required outputs

When run, the program must print to stdout:

1. **Overall summary** — total income, total expenses, and net balance.
2. **Category table** — each category's transaction count and total spend.
3. **Top 3 expense categories** — sorted by most negative spend.

Example output (values will differ based on your data):

```
====================================================
  LEDGER SUMMARY
====================================================
  Transactions :   20
  Total income :    +$6250.00
  Total expenses:   -$753.74
  Net balance  :   +$5496.26
----------------------------------------------------
  TRANSACTIONS BY CATEGORY
----------------------------------------------------
  Category       Count         Spend
----------------------------------------------------
  dining             4       -$137.55
  groceries          4       -$275.70
  income             4      +$6250.00
  transport          4       -$115.50
  utilities          4       -$285.49
----------------------------------------------------
  TOP 3 EXPENSE CATEGORIES
----------------------------------------------------
  1. utilities       -$285.49
  2. groceries       -$275.70
  3. dining          -$137.55
====================================================
```

---

## Acceptance checklist

Work through the source code in `src/index.ts` and tick each item:

- [ ] The `Transaction` interface is defined with the correct field names and types.
- [ ] The file is loaded using `readFileSync` with the path resolved via `import.meta.url`.
- [ ] `computeSummary` is a pure function — it does not mutate its input array.
- [ ] The function accepts `readonly Transaction[]` to enforce immutability.
- [ ] The empty array case returns zeros without crashing.
- [ ] `totalIncome` counts only transactions where `amount > 0`.
- [ ] `totalExpenses` counts only transactions where `amount < 0`.
- [ ] `countByCategory` and `spendByCategory` are built using a single loop.
- [ ] Index signature accesses (`record[key]`) are narrowed with `?? 0` before arithmetic.
- [ ] `topCategories` filters out income categories and sorts by most negative spend first.
- [ ] The output table aligns columns using `padEnd` / `padStart`.
- [ ] Running the file prints a complete summary with no TypeScript errors.

---

## How to extend (stretch goals)

- Accept the JSON file path as a CLI argument: `process.argv[2]`.
- Filter by date range: only show transactions within a given month.
- Add a `--json` flag that outputs the summary as JSON instead of a table.
- Validate the JSON shape at runtime using Zod (covered on Day 5).
