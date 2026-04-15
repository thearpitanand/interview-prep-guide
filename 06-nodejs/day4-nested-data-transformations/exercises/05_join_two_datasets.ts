/**
 * Exercise 05 — Join Two Datasets
 *
 * Topics: left join, inner join, hash-map for O(n + m) performance
 *
 * Implements:
 *   leftJoin  — every left row appears; right is undefined if no match
 *   innerJoin — only rows with a match on both sides
 *
 * Both functions accept key-extractor functions so the join key can be any
 * field, not just "id". The right side is hashed once for O(1) per lookup.
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------

type User = {
  userId: string;
  name: string;
  tier: "bronze" | "silver" | "gold";
};

type Order = {
  orderId: string;
  userId: string;
  total: number;
  status: "pending" | "shipped" | "delivered";
};

// ---------------------------------------------------------------------------
// leftJoin
// ---------------------------------------------------------------------------

/**
 * Returns every row from `left`. If a matching row exists in `right`
 * (by key), it is merged as `{ ...left, right: matchingRow }`.
 * If no match, `right` is `undefined` in the output.
 */
export function leftJoin<L, R>(
  left: readonly L[],
  right: readonly R[],
  leftKey:  (l: L) => string,
  rightKey: (r: R) => string
): Array<L & { right: R | undefined }> {
  throw new Error("TODO: implement leftJoin");
}

// ---------------------------------------------------------------------------
// innerJoin
// ---------------------------------------------------------------------------

/**
 * Returns only rows where a match exists on both sides.
 * Uses flatMap: returns [] for non-matches, [mergedRow] for matches.
 */
export function innerJoin<L, R>(
  left: readonly L[],
  right: readonly R[],
  leftKey:  (l: L) => string,
  rightKey: (r: R) => string
): Array<L & { right: R }> {
  throw new Error("TODO: implement innerJoin");
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  const users: User[] = [
    { userId: "U1", name: "Ava Martin",  tier: "gold"   },
    { userId: "U2", name: "Ben Carter",  tier: "silver" },
    { userId: "U3", name: "Clara Stone", tier: "bronze" },
    { userId: "U4", name: "Dan Wells",   tier: "gold"   }, // no orders
  ];

  const orders: Order[] = [
    { orderId: "O100", userId: "U1", total: 299.99, status: "delivered" },
    { orderId: "O101", userId: "U1", total: 149.00, status: "shipped"   },
    { orderId: "O102", userId: "U2", total: 89.99,  status: "pending"   },
    { orderId: "O103", userId: "U3", total: 49.99,  status: "delivered" },
    { orderId: "O999", userId: "U9", total: 1.00,   status: "pending"   }, // orphan — no user
  ];

  // ---- leftJoin: users left-joined to orders ----
  // Every user appears; orders with no matching user are irrelevant here
  const usersWithOrders = leftJoin(
    users,
    orders,
    u => u.userId,
    o => o.userId
  );

  assert.equal(usersWithOrders.length, 4); // all 4 users

  // U1 matches multiple orders — leftJoin picks the first hit (Map stores last insertion)
  // This join is many-to-one (many orders per user) — the right Map stores the last order for U1
  // For proper one-to-many, use groupBy on right side first
  const ava = usersWithOrders.find(r => r.userId === "U1");
  assert.ok(ava !== undefined);
  assert.ok(ava.right !== undefined); // Ava has orders

  // U4 has no orders → right is undefined
  const dan = usersWithOrders.find(r => r.userId === "U4");
  assert.ok(dan !== undefined);
  assert.equal(dan.right, undefined);

  // ---- leftJoin: orders left-joined to users ----
  // Every order appears; O999 has no matching user
  const ordersWithUsers = leftJoin(
    orders,
    users,
    o => o.userId,
    u => u.userId
  );

  assert.equal(ordersWithUsers.length, 5); // all 5 orders

  const orphan = ordersWithUsers.find(r => r.orderId === "O999");
  assert.ok(orphan !== undefined);
  assert.equal(orphan.right, undefined); // no matching user

  const o100 = ordersWithUsers.find(r => r.orderId === "O100");
  assert.ok(o100 !== undefined);
  assert.equal(o100.right?.name, "Ava Martin");
  assert.equal(o100.right?.tier, "gold");

  // ---- innerJoin: only rows with matches on both sides ----
  const matched = innerJoin(
    orders,
    users,
    o => o.userId,
    u => u.userId
  );

  // O999 (userId: U9) has no matching user → excluded
  assert.equal(matched.length, 4); // O100, O101, O102, O103

  const matchedIds = matched.map(r => r.orderId).sort();
  assert.deepEqual(matchedIds, ["O100", "O101", "O102", "O103"]);

  // Verify merged fields
  const m100 = matched.find(r => r.orderId === "O100");
  assert.ok(m100 !== undefined);
  assert.equal(m100.status,     "delivered");
  assert.equal(m100.right.name, "Ava Martin");
  assert.equal(m100.right.tier, "gold");

  // ---- edge cases ----

  // Both empty
  assert.deepEqual(leftJoin([], [], u => "", r => ""), []);
  assert.deepEqual(innerJoin([], [], u => "", r => ""), []);

  // Left empty
  assert.deepEqual(
    leftJoin([] as User[], users, u => u.userId, u => u.userId),
    []
  );

  // Right empty → all left rows have right: undefined
  const noRight = leftJoin(users, [] as Order[], u => u.userId, o => o.userId);
  assert.equal(noRight.length, 4);
  assert.ok(noRight.every(r => r.right === undefined));

  // Right empty → innerJoin produces nothing
  assert.deepEqual(
    innerJoin(users, [] as Order[], u => u.userId, o => o.userId),
    []
  );

  // ---- leftJoin preserves all left fields ----
  const r = leftJoin(
    [{ userId: "U1", name: "Ava Martin", tier: "gold" as const }],
    [{ orderId: "O100", userId: "U1", total: 299.99, status: "delivered" as const }],
    u => u.userId,
    o => o.userId
  );
  assert.equal(r[0]?.name,          "Ava Martin");
  assert.equal(r[0]?.right?.orderId, "O100");

  console.log("All tests passed!");
}
