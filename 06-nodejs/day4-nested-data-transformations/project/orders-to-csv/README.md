# orders-to-csv — Day 4 Project

## Run

```bash
npx tsx day4-nested-data-transformations/project/orders-to-csv/src/index.ts
```

Run from the `06-nodejs/` directory.

---

## What It Does

Reads a deeply nested `data/customers.json` and produces two flat CSV files in `out/`.

### Input shape

```
customers.json
└── customers[]
    ├── customerId, name, email, tier
    └── orders[]
        ├── orderId, placedAt, status
        └── items[]
            └── sku, name, qty, unitPrice
```

8 customers, 19 orders, ~50 line items. Realistic shop data with ISO dates and proper pricing.

### Output 1 — `out/line_items.csv`

One row per line item. All ancestor fields are copied down to each row.

Columns:
| Column | Description |
|--------|-------------|
| `customerId` | Customer identifier |
| `customerName` | Customer display name |
| `email` | Customer email |
| `tier` | `bronze` / `silver` / `gold` |
| `orderId` | Order identifier |
| `placedAt` | Date only (`YYYY-MM-DD`) |
| `status` | `pending` / `shipped` / `delivered` |
| `sku` | Product SKU |
| `itemName` | Product display name |
| `qty` | Quantity ordered |
| `unitPrice` | Price per unit |
| `lineTotal` | `qty × unitPrice`, rounded to 2 dp |

### Output 2 — `out/customer_totals.csv`

One row per customer with aggregated stats.

Columns:
| Column | Description |
|--------|-------------|
| `customerId` | Customer identifier |
| `name` | Customer display name |
| `email` | Customer email |
| `tier` | Customer tier |
| `orderCount` | Number of distinct orders |
| `itemCount` | Total quantity of all items across all orders |
| `totalSpend` | Sum of all `lineTotal` values, rounded to 2 dp |

---

## Key implementation details

- **No CSV library** — `toCSV` in `transforms.ts` writes CSV by hand, correctly quoting values that contain commas, double-quotes, or newlines (RFC 4180 compatible for these cases).
- **No mutation** — all transform functions return new data structures; inputs are never modified.
- **`out/` created if missing** — `mkdirSync(outDir, { recursive: true })` handles this.
- **Empty arrays safe** — a customer with no orders contributes zero line-item rows; an order with no items also contributes zero rows. No crashes.

---

## Acceptance checklist

- [ ] `out/line_items.csv` has a header row + one data row per line item
- [ ] `out/customer_totals.csv` has a header row + 8 data rows (one per customer)
- [ ] `lineTotal` values are correct (spot-check: LAPTOP-PRO-15 × 1 = 1299.00)
- [ ] `totalSpend` for a gold customer is higher than for a bronze customer (in this dataset)
- [ ] Running the command twice produces the same output (pure, deterministic)
- [ ] No `any` in the TypeScript source

---

## File layout

```
orders-to-csv/
├── README.md
├── data/
│   └── customers.json       ← input (8 customers, 19 orders)
├── out/
│   ├── line_items.csv       ← generated on run
│   └── customer_totals.csv  ← generated on run
└── src/
    ├── transforms.ts        ← pure functions (no I/O)
    └── index.ts             ← entry point (reads, transforms, writes)
```
