/**
 * transforms.ts — Pure data transformation functions
 *
 * No I/O here. Every function is pure: same input → same output, no side effects.
 * These are the same patterns from the Day 4 exercises, adapted for the project types.
 */

// ---------------------------------------------------------------------------
// Input types (matching customers.json)
// ---------------------------------------------------------------------------

export type LineItem = {
  sku: string;
  name: string;
  qty: number;
  unitPrice: number;
};

export type Order = {
  orderId: string;
  placedAt: string;
  status: string;
  items: LineItem[];
};

export type Customer = {
  customerId: string;
  name: string;
  email: string;
  tier: string;
  orders: Order[];
};

// ---------------------------------------------------------------------------
// Output types
// ---------------------------------------------------------------------------

/** One row per line item — used for line_items.csv */
export type FlatLineItem = {
  customerId: string;
  customerName: string;
  email: string;
  tier: string;
  orderId: string;
  placedAt: string;
  status: string;
  sku: string;
  itemName: string;
  qty: number;
  unitPrice: number;
  lineTotal: number;
};

/** Per-customer aggregate — used for customer_totals.csv */
export type CustomerTotal = {
  customerId: string;
  name: string;
  email: string;
  tier: string;
  orderCount: number;
  itemCount: number;
  totalSpend: number;
};

// ---------------------------------------------------------------------------
// denormalize — flatten customer → order → item hierarchy into one row per item
// ---------------------------------------------------------------------------

export function denormalize(customers: readonly Customer[]): FlatLineItem[] {
  return customers.flatMap(customer =>
    customer.orders.flatMap(order =>
      order.items.map(item => ({
        customerId:   customer.customerId,
        customerName: customer.name,
        email:        customer.email,
        tier:         customer.tier,
        orderId:      order.orderId,
        placedAt:     order.placedAt.slice(0, 10), // ISO date, date part only
        status:       order.status,
        sku:          item.sku,
        itemName:     item.name,
        qty:          item.qty,
        unitPrice:    item.unitPrice,
        lineTotal:    round2(item.qty * item.unitPrice),
      }))
    )
  );
}

// ---------------------------------------------------------------------------
// groupBy — generic partitioning
// ---------------------------------------------------------------------------

export function groupBy<T>(
  arr: readonly T[],
  fn: (item: T) => string
): Record<string, T[]> {
  const result: Record<string, T[]> = {};
  for (const item of arr) {
    const key = fn(item);
    if (result[key] === undefined) result[key] = [];
    result[key]!.push(item);
  }
  return result;
}

// ---------------------------------------------------------------------------
// aggregateCustomers — compute per-customer totals from flat rows
// ---------------------------------------------------------------------------

export function aggregateCustomers(
  flatRows: readonly FlatLineItem[],
  customers: readonly Customer[]
): CustomerTotal[] {
  const grouped = groupBy(flatRows, r => r.customerId);

  return customers.map(customer => {
    const rows = grouped[customer.customerId] ?? [];

    // Count distinct orders
    const orderIds = new Set(rows.map(r => r.orderId));

    return {
      customerId: customer.customerId,
      name:       customer.name,
      email:      customer.email,
      tier:       customer.tier,
      orderCount: orderIds.size,
      itemCount:  rows.reduce((sum, r) => sum + r.qty, 0),
      totalSpend: round2(rows.reduce((sum, r) => sum + r.lineTotal, 0)),
    };
  });
}

// ---------------------------------------------------------------------------
// toCSV — serialize an array of objects to a CSV string
//
// - First row is the header (keys of the first object, in definition order)
// - Values are quoted if they contain commas, double-quotes, or newlines
// - Double-quotes inside values are escaped as ""
// - No external library needed
// ---------------------------------------------------------------------------

export function toCSV(rows: readonly Record<string, unknown>[]): string {
  if (rows.length === 0) return "";

  const firstRow = rows[0];
  if (firstRow === undefined) return "";
  const headers = Object.keys(firstRow);

  const escape = (val: unknown): string => {
    const str = val === null || val === undefined ? "" : String(val);
    // Quote if the value contains a comma, double-quote, or newline
    if (str.includes(",") || str.includes('"') || str.includes("\n")) {
      return `"${str.replace(/"/g, '""')}"`;
    }
    return str;
  };

  const lines: string[] = [headers.join(",")];

  for (const row of rows) {
    const cells = headers.map(h => escape(row[h]));
    lines.push(cells.join(","));
  }

  return lines.join("\n") + "\n";
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function round2(n: number): number {
  return Math.round(n * 100) / 100;
}
