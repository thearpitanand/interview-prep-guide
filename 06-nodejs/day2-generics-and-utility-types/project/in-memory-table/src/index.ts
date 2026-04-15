/**
 * In-Memory Table — Driver
 *
 * Demonstrates Table<User> and Table<Transaction> with typed CRUD,
 * where, pluck, groupBy, and count operations.
 *
 * Run: npx tsx day2-generics-and-utility-types/project/in-memory-table/src/index.ts
 */
import { Table } from "./table.js";
import usersRaw from "../data/users.json" with { type: "json" };
import transactionsRaw from "../data/transactions.json" with { type: "json" };

// ---------- Types ----------

interface User {
  /* TODO: define User */
}

interface Transaction {
  /* TODO: define Transaction */
}

// ---------- Seed Tables ----------

const userTable = new Table<User>();
const txTable = new Table<Transaction>();

// JSON data is untyped — cast once here at the boundary
for (const raw of usersRaw) {
  userTable.insert(raw as User);
}
for (const raw of transactionsRaw) {
  txTable.insert(raw as Transaction);
}

// ---------- Demo: User Table ----------

console.log("=== User Table ===");
console.log(`Total users: ${userTable.count()}`);

// findById
const alice = userTable.findById("u-001");
console.log(`\nfindById("u-001"):`, alice?.name);

// update — merge patch
const updated = userTable.update("u-001", { age: 33 });
console.log(`After update age: ${updated.age}`);
console.log(`Name unchanged: ${updated.name}`);

// where — find admins
const admins = userTable.where((u) => u.role === "admin");
console.log(`\nAdmins (${admins.length}):`);
admins.forEach((u) => console.log(`  - ${u.name} (${u.email})`));

// pluck — all emails, typed as string[]
const emails = userTable.pluck("email");
console.log(`\nAll emails (pluck):`, emails.slice(0, 3), "...");

// groupBy — group by role
// Type-safe: userTable.groupBy("nope") would be a compile error
const byRole = userTable.groupBy("role");
console.log(`\ngroupBy("role"):`);
for (const [role, members] of Object.entries(byRole)) {
  console.log(`  ${role}: ${members.map((m) => m.name).join(", ")}`);
}

// delete — remove a user
const deleted = userTable.delete("u-010");
console.log(`\nDeleted u-010: ${deleted}`);
console.log(`Count after delete: ${userTable.count()}`);
console.log(`findById after delete: ${userTable.findById("u-010")}`);

// ---------- Demo: Transaction Table ----------

console.log("\n=== Transaction Table ===");
console.log(`Total transactions: ${txTable.count()}`);

// where — all credits
const credits = txTable.where((tx) => tx.type === "credit");
console.log(`\nCredit transactions: ${credits.length}`);
const totalCredit = credits.reduce((sum, tx) => sum + tx.amount, 0);
console.log(`Total credits: $${totalCredit.toFixed(2)}`);

// where — transactions over $200
const big = txTable.where((tx) => tx.amount > 200);
console.log(`\nTransactions over $200 (${big.length}):`);
big.forEach((tx) => console.log(`  ${tx.id}: $${tx.amount} — ${tx.description}`));

// groupBy — by type
const byType = txTable.groupBy("type");
const creditCount = byType["credit"]?.length ?? 0;
const debitCount  = byType["debit"]?.length ?? 0;
console.log(`\ngroupBy("type"): credit=${creditCount}, debit=${debitCount}`);

// pluck — all amounts, typed as number[]
const amounts = txTable.pluck("amount");
const maxAmount = Math.max(...amounts);
console.log(`\nMax transaction amount: $${maxAmount}`);

// update — amend a transaction description
const txUpdated = txTable.update("tx-001", { description: "Monthly salary" });
console.log(`\nUpdated tx-001 description: "${txUpdated.description}"`);
console.log(`Amount unchanged: $${txUpdated.amount}`);

// ---------- Type Safety Demo ----------

console.log("\n=== Type Safety ===");
// The following lines demonstrate what IS type-safe:
// userTable.groupBy("role")   — OK, "role" is keyof User
// userTable.pluck("email")    — OK, returns string[]
// userTable.pluck("age")      — OK, returns number[]
//
// The following would be COMPILE ERRORS (uncomment to verify):
// userTable.groupBy("nope")   — Error: Argument of type '"nope"' is not assignable
// userTable.pluck("nope")     — Error: same
// userTable.update("u-001", { id: "new" })  — Error: id is in Omit<User, "id">

const ageList = userTable.pluck("age"); // number[]
const oldest = Math.max(...ageList);
console.log(`Oldest user age: ${oldest}`);
console.log("\nDriver completed successfully.");
