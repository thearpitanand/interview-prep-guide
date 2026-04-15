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
  throw new Error("TODO: implement denormalize");
}

// ---------------------------------------------------------------------------
// groupBy — generic partitioning
// ---------------------------------------------------------------------------

export function groupBy<T>(
  arr: readonly T[],
  fn: (item: T) => string
): Record<string, T[]> {
  throw new Error("TODO: implement groupBy");
}

// ---------------------------------------------------------------------------
// aggregateCustomers — compute per-customer totals from flat rows
// ---------------------------------------------------------------------------

export function aggregateCustomers(
  flatRows: readonly FlatLineItem[],
  customers: readonly Customer[]
): CustomerTotal[] {
  throw new Error("TODO: implement aggregateCustomers");
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
  throw new Error("TODO: implement toCSV");
}
