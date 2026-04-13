/**
 * Exercise 07 — Denormalize Nested Arrays
 *
 * Topics: flatMap for multi-level flattening, copying ancestor fields to leaf rows,
 *         handling empty arrays without crashing
 *
 * Given:  Customer → Orders[] → Items[]
 * Output: One flat row per line item with all ancestor fields copied down.
 *
 * This is the most common ETL transformation: turn a nested API response
 * into the flat table your CSV or analytics system expects.
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Input types (nested)
// ---------------------------------------------------------------------------

type LineItem = {
  sku: string;
  itemName: string;
  qty: number;
  unitPrice: number;
};

type Order = {
  orderId: string;
  placedAt: string; // ISO date string
  status: "pending" | "shipped" | "delivered";
  items: LineItem[];
};

type Customer = {
  customerId: string;
  name: string;
  tier: "bronze" | "silver" | "gold";
  orders: Order[];
};

// ---------------------------------------------------------------------------
// Output type (flat)
// ---------------------------------------------------------------------------

type FlatLineItem = {
  customerId: string;
  customerName: string;
  tier: "bronze" | "silver" | "gold";
  orderId: string;
  placedAt: string;
  status: "pending" | "shipped" | "delivered";
  sku: string;
  itemName: string;
  qty: number;
  unitPrice: number;
  lineTotal: number; // computed: qty * unitPrice
};

// ---------------------------------------------------------------------------
// denormalize
// ---------------------------------------------------------------------------

/**
 * Flattens a customer/order/item hierarchy into one row per line item.
 *
 * Uses flatMap at each level:
 *   customers.flatMap → orders.flatMap → items.map
 *
 * Empty orders or items arrays produce zero rows for that customer/order —
 * no crash, no undefined rows.
 */
export function denormalize(customers: readonly Customer[]): FlatLineItem[] {
  return customers.flatMap(customer =>
    customer.orders.flatMap(order =>
      order.items.map(item => ({
        customerId:   customer.customerId,
        customerName: customer.name,
        tier:         customer.tier,
        orderId:      order.orderId,
        placedAt:     order.placedAt,
        status:       order.status,
        sku:          item.sku,
        itemName:     item.itemName,
        qty:          item.qty,
        unitPrice:    item.unitPrice,
        lineTotal:    Math.round(item.qty * item.unitPrice * 100) / 100,
      }))
    )
  );
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  // 2 customers × 3 orders × 2 items = 12 rows (when all are present)
  const customers: Customer[] = [
    {
      customerId: "C001",
      name: "Ava Martin",
      tier: "gold",
      orders: [
        {
          orderId: "O100",
          placedAt: "2024-01-15",
          status: "delivered",
          items: [
            { sku: "WIDGET-A", itemName: "Widget Alpha", qty: 2, unitPrice: 29.99 },
            { sku: "GADGET-B", itemName: "Gadget Beta",  qty: 1, unitPrice: 49.99 },
          ],
        },
        {
          orderId: "O101",
          placedAt: "2024-02-03",
          status: "shipped",
          items: [
            { sku: "CABLE-C",  itemName: "USB Cable",   qty: 3, unitPrice: 9.99  },
            { sku: "WIDGET-A", itemName: "Widget Alpha", qty: 1, unitPrice: 29.99 },
          ],
        },
        {
          orderId: "O102",
          placedAt: "2024-03-10",
          status: "pending",
          items: [
            { sku: "BAG-D",    itemName: "Laptop Bag",   qty: 1, unitPrice: 79.00 },
            { sku: "STAND-E",  itemName: "Monitor Stand", qty: 2, unitPrice: 39.50 },
          ],
        },
      ],
    },
    {
      customerId: "C002",
      name: "Ben Carter",
      tier: "silver",
      orders: [
        {
          orderId: "O200",
          placedAt: "2024-01-22",
          status: "delivered",
          items: [
            { sku: "KBOARD-F", itemName: "Mechanical Keyboard", qty: 1, unitPrice: 129.00 },
            { sku: "MOUSE-G",  itemName: "Ergonomic Mouse",     qty: 1, unitPrice: 59.99  },
          ],
        },
        {
          orderId: "O201",
          placedAt: "2024-02-14",
          status: "shipped",
          items: [
            { sku: "HDMI-H",  itemName: "HDMI Cable 2m",  qty: 2, unitPrice: 14.99 },
            { sku: "CABLE-C", itemName: "USB Cable",      qty: 4, unitPrice: 9.99  },
          ],
        },
        {
          orderId: "O202",
          placedAt: "2024-04-01",
          status: "pending",
          items: [
            { sku: "STAND-E", itemName: "Monitor Stand",   qty: 1, unitPrice: 39.50 },
            { sku: "BAG-D",   itemName: "Laptop Bag",      qty: 1, unitPrice: 79.00 },
          ],
        },
      ],
    },
  ];

  const rows = denormalize(customers);

  // Total: 2 customers × 3 orders × 2 items = 12 rows
  assert.equal(rows.length, 12);

  // ---- First row: C001, O100, WIDGET-A ----
  const firstRow = rows.find(r => r.orderId === "O100" && r.sku === "WIDGET-A");
  assert.ok(firstRow !== undefined, "First row not found");
  assert.equal(firstRow.customerId,   "C001");
  assert.equal(firstRow.customerName, "Ava Martin");
  assert.equal(firstRow.tier,         "gold");
  assert.equal(firstRow.qty,          2);
  assert.ok(Math.abs(firstRow.unitPrice - 29.99) < 0.001);
  assert.ok(Math.abs(firstRow.lineTotal - 59.98) < 0.001); // 2 × 29.99

  // ---- lineTotal correctness for a few rows ----
  const gadgetRow = rows.find(r => r.sku === "GADGET-B");
  assert.ok(gadgetRow !== undefined);
  assert.ok(Math.abs(gadgetRow.lineTotal - 49.99) < 0.001); // 1 × 49.99

  const cableO101 = rows.find(r => r.orderId === "O101" && r.sku === "CABLE-C");
  assert.ok(cableO101 !== undefined);
  assert.ok(Math.abs(cableO101.lineTotal - 29.97) < 0.001); // 3 × 9.99

  // ---- All C002 rows have the right customerId ----
  const c002Rows = rows.filter(r => r.customerId === "C002");
  assert.equal(c002Rows.length, 6); // 3 orders × 2 items
  assert.ok(c002Rows.every(r => r.customerName === "Ben Carter"));
  assert.ok(c002Rows.every(r => r.tier === "silver"));

  // ---- Order fields correctly propagated ----
  const pendingRows = rows.filter(r => r.status === "pending");
  assert.equal(pendingRows.length, 4); // O102 (2 items) + O202 (2 items)

  // ---- Edge cases ----

  // Customer with no orders → 0 rows
  const noOrderCustomer: Customer = {
    customerId: "C999",
    name: "Ghost User",
    tier: "bronze",
    orders: [],
  };
  const rowsWithEmpty = denormalize([noOrderCustomer]);
  assert.equal(rowsWithEmpty.length, 0);

  // Order with no items → 0 rows for that order
  const emptyOrder: Customer = {
    customerId: "C998",
    name: "Sparse User",
    tier: "bronze",
    orders: [
      { orderId: "O998", placedAt: "2024-05-01", status: "pending", items: [] },
      { orderId: "O997", placedAt: "2024-05-02", status: "pending", items: [
        { sku: "WIDGET-A", itemName: "Widget Alpha", qty: 1, unitPrice: 29.99 },
      ]},
    ],
  };
  const sparseRows = denormalize([emptyOrder]);
  assert.equal(sparseRows.length, 1);
  assert.equal(sparseRows[0]?.orderId, "O997");

  // Empty input
  assert.deepEqual(denormalize([]), []);

  // ---- Row ordering: follows input nesting order ----
  // First row should be the first item of the first order of the first customer
  assert.equal(rows[0]?.customerId, "C001");
  assert.equal(rows[0]?.orderId,    "O100");
  assert.equal(rows[0]?.sku,        "WIDGET-A");

  // 7th row (index 6) should be first item of C002's first order
  assert.equal(rows[6]?.customerId, "C002");
  assert.equal(rows[6]?.orderId,    "O200");

  console.log("All tests passed!");
}
