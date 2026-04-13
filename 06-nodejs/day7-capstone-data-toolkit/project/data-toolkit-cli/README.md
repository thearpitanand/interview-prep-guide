# data-toolkit-cli

A composable CLI for reading, transforming, and exporting structured data (JSON, NDJSON, CSV).

## Run

```bash
# From the repo root:
npx tsx day7-capstone-data-toolkit/project/data-toolkit-cli/src/index.ts <command> [options]

# From this directory:
npx tsx src/index.ts <command> [options]
```

## Run Tests

```bash
# From this directory:
npx tsx --test tests/*.test.ts
```

---

## Subcommands

### `flatten <file>`

Recursively flatten nested JSON objects into dot-separated keys.

```bash
npx tsx src/index.ts flatten fixtures/users.json
npx tsx src/index.ts flatten fixtures/users.json --format csv
npx tsx src/index.ts flatten fixtures/users.json --format json
```

**Options:**
- `--format json|csv|table` (default: `table`)
- `--input json|ndjson|csv` (default: inferred from extension)

**Expected output (table):**
```
+----+-------+-----+-------+------------------+------------------+
| id | name  | age | role  | address.city     | address.country  |
+----+-------+-----+-------+------------------+------------------+
| 1  | Alice | 30  | admin | New York         | US               |
...
```

---

### `group <file> --by <key> [--agg count|sum:<col>]`

Group records by a key and apply an aggregation.

```bash
npx tsx src/index.ts group fixtures/orders.json --by category --agg count
npx tsx src/index.ts group fixtures/orders.json --by category --agg sum:amount
npx tsx src/index.ts group fixtures/people.csv --by department --agg sum:salary --format json
```

**Options:**
- `--by <key>` — field to group by (required)
- `--agg count|sum:<col>` — aggregation (default: `count`)
- `--format json|csv|table` (default: `table`)

**Expected output (`--by category --agg count`):**
```
+-------------+-------+
| category    | count |
+-------------+-------+
| electronics | 3     |
| education   | 2     |
| furniture   | 2     |
+-------------+-------+
```

---

### `join <left.json> <right.json> --on <leftKey>=<rightKey> [--type left|inner]`

Join two files on a key. Supports left join (default) and inner join.

```bash
npx tsx src/index.ts join fixtures/users.json fixtures/orders.json --on id=userId
npx tsx src/index.ts join fixtures/users.json fixtures/orders.json --on id=userId --type inner
npx tsx src/index.ts join fixtures/users.json fixtures/orders.json --on id=userId --format json
```

**Options:**
- `--on <leftKey>=<rightKey>` — join condition (required)
- `--type inner|left` — join type (default: `left`)
- `--format json|csv|table` (default: `table`)

**Notes:**
- Left join: all rows from the left file appear; unmatched rows have no right-side values.
- Inner join: only rows that match in both files.

---

### `pivot <file> --row <rowKey> --col <colKey> --value <valueKey>`

Rotate unique values of `--col` into column headers, filling cells with `--value`.

```bash
npx tsx src/index.ts pivot fixtures/orders.json --row category --col status --value amount
npx tsx src/index.ts pivot fixtures/orders.json --row category --col status --value amount --format json
```

**Options:**
- `--row <key>` — field to use as row identifier (required)
- `--col <key>` — field whose unique values become column headers (required)
- `--value <key>` — field to fill into cells (required)
- `--format json|csv|table` (default: `table`)

**Expected output:**
```
+-------------+---------+-----------+---------+
| category    | shipped | delivered | pending |
+-------------+---------+-----------+---------+
| electronics | 1200    | 60        | null    |
| education   | null    | 45        | null    |
| furniture   | null    | null      | 350     |
+-------------+---------+-----------+---------+
```

---

### `validate <file> --schema <name>`

Validate each record against a named Zod schema. Prints valid/invalid counts and error details.

Available schemas: `user`, `transaction`, `order`

```bash
npx tsx src/index.ts validate fixtures/users.json --schema user
npx tsx src/index.ts validate fixtures/orders.json --schema order
npx tsx src/index.ts validate fixtures/transactions.ndjson --schema transaction
```

**Expected output:**
```
Schema:  user
File:    fixtures/users.json
Total:   5
Valid:   5
Invalid: 0
```

---

### `table <file>`

Pretty-print any JSON array (or CSV file) as an ASCII table.

```bash
npx tsx src/index.ts table fixtures/users.json
npx tsx src/index.ts table fixtures/people.csv
npx tsx src/index.ts table fixtures/orders.json
```

---

## Global Options

| Option | Values | Default |
|--------|--------|---------|
| `--format` | `json`, `csv`, `table` | `table` |
| `--input` | `json`, `ndjson`, `csv` | inferred from extension |

---

## Acceptance Checklist

- [ ] `flatten` flattens nested JSON, outputs JSON/CSV/table
- [ ] `group` groups by any string key with count or sum aggregation
- [ ] `join` performs left and inner join, merges fields from both sides
- [ ] `pivot` rotates column values into headers, fills nulls for missing cells
- [ ] `validate` checks all records against named schemas, reports valid/invalid counts
- [ ] `table` renders any JSON array or CSV as an ASCII table
- [ ] All commands support `--format json|csv|table`
- [ ] Errors go to stderr, output goes to stdout
- [ ] Exit code 1 on errors, 0 on success
- [ ] All transform functions are pure and unit-testable
- [ ] Tests pass: `npx tsx --test tests/*.test.ts`

---

## Project Structure

```
src/
  index.ts              CLI entry: parse argv, dispatch commands
  args.ts               Stdlib argv parser, typed option interfaces
  io/
    read.ts             Read JSON / NDJSON / CSV into typed arrays
    write.ts            Format typed arrays as JSON / CSV / ASCII table
    table.ts            Pure ASCII table renderer (no deps)
  transforms/
    flatten.ts          Recursive object flattening
    group.ts            GroupBy with count/sum aggregation
    join.ts             Left and inner join
    pivot.ts            Pivot rows into columns
  schemas/
    index.ts            Zod schema registry (user, transaction, order)
  commands/
    flatten.ts          Thin handler: read → flatten → write
    group.ts            Thin handler: read → group → write
    join.ts             Thin handler: read left + right → join → write
    pivot.ts            Thin handler: read → pivot → write
    validate.ts         Read → validate each row → print report
    table.ts            Read → render as ASCII table
fixtures/
  users.json
  orders.json
  transactions.ndjson
  people.csv
tests/
  transforms.test.ts   Unit tests for pure transforms (no I/O)
  commands.test.ts     Integration tests using fixture files
```
