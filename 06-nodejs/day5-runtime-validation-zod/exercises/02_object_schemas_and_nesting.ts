/**
 * Day 5 — Exercise 02: Object Schemas and Nesting
 *
 * Build a UserSchema with nested AddressSchema and CompanySchema.
 * Derive types with z.infer. Test happy paths and deliberate failures.
 * Explore .strict(), .partial(), .pick(), .omit(), and .extend().
 *
 * Run: npx tsx day5-runtime-validation-zod/exercises/02_object_schemas_and_nesting.ts
 */
import { z } from "zod";
import assert from "node:assert/strict";

// ---------- SCHEMAS ----------

// TODO: define AddressSchema — object with street (string min 1), city (string min 1),
//       state (string length 2), zip (string regex /^\d{5}$/), country (string default "US")
export const AddressSchema = z.unknown();

// TODO: define CompanySchema — object with name (string min 1), domain (string url),
//       size (enum: "startup" | "small" | "medium" | "enterprise")
export const CompanySchema = z.unknown();

// TODO: define UserSchema — object with id (uuid), email, name (min 1), age (int 0-150, optional),
//       address (AddressSchema), company (CompanySchema, optional),
//       tags (array of string, default []), active (boolean, default true)
export const UserSchema = z.unknown();

// Derived types — no separate interfaces needed
type Address = z.infer<typeof AddressSchema>;
type Company = z.infer<typeof CompanySchema>;
type User = z.infer<typeof UserSchema>;

// TODO: define UserSummarySchema — pick id, email, name, active from UserSchema
export const UserSummarySchema = z.unknown();
type UserSummary = z.infer<typeof UserSummarySchema>;

// TODO: define CreateUserSchema — omit id, active, tags from UserSchema
export const CreateUserSchema = z.unknown();
type CreateUser = z.infer<typeof CreateUserSchema>;

// TODO: define PatchUserSchema — all fields optional, but id required
export const PatchUserSchema = z.unknown();
type PatchUser = z.infer<typeof PatchUserSchema>;

// TODO: define AdminUserSchema — extend UserSchema with role (literal "admin") and permissions (string[])
export const AdminUserSchema = z.unknown();
type AdminUser = z.infer<typeof AdminUserSchema>;

// ---------- TEST DATA ----------

const rawValidUser = {
  id: "550e8400-e29b-41d4-a716-446655440000",
  email: "alice@example.com",
  name: "Alice Smith",
  age: 30,
  address: {
    street: "123 Main St",
    city: "Springfield",
    state: "IL",
    zip: "62701",
  },
  company: {
    name: "Acme Corp",
    domain: "https://acme.com",
    size: "medium",
  },
};

// Deliberate failures
const missingEmail = {
  id: "550e8400-e29b-41d4-a716-446655440001",
  name: "Bob",
  address: { street: "1 Oak Ave", city: "Chicago", state: "IL", zip: "60601" },
};

const badNestedAddress = {
  id: "550e8400-e29b-41d4-a716-446655440002",
  email: "carol@example.com",
  name: "Carol",
  address: {
    street: "99 Elm St",
    city: "Dallas",
    state: "TEXAS", // too long — must be 2 chars
    zip: "75201",
  },
};

const badCompanySize = {
  id: "550e8400-e29b-41d4-a716-446655440003",
  email: "dave@example.com",
  name: "Dave",
  address: { street: "5 Pine Rd", city: "Austin", state: "TX", zip: "78701" },
  company: { name: "BigCo", domain: "https://bigco.io", size: "giant" }, // invalid enum
};

// ---------- TESTS ----------

// Happy path — full user
const parsedUser = UserSchema.parse(rawValidUser);
assert.equal(parsedUser.email, "alice@example.com");
assert.equal(parsedUser.address.country, "US"); // default applied
assert.deepEqual(parsedUser.tags, []); // default applied
assert.equal(parsedUser.active, true); // default applied
assert.equal(parsedUser.company?.size, "medium");

// Type checks (runtime)
const u: User = parsedUser;
assert.equal(typeof u.id, "string");
assert.equal(typeof u.address.zip, "string");

// safeParse failures
const r1 = UserSchema.safeParse(missingEmail);
assert.equal(r1.success, false);
if (!r1.success) {
  const flat = r1.error.flatten();
  assert.ok(flat.fieldErrors["email"] !== undefined, "Should report missing email");
}

const r2 = UserSchema.safeParse(badNestedAddress);
assert.equal(r2.success, false);
if (!r2.success) {
  // path should include "address" and "state"
  const statePath = r2.error.issues.some(
    (i) => i.path.includes("address") && i.path.includes("state")
  );
  assert.ok(statePath, "Error path should point into address.state");
}

const r3 = UserSchema.safeParse(badCompanySize);
assert.equal(r3.success, false);
if (!r3.success) {
  assert.ok(
    r3.error.issues.some((i) => i.path.includes("company") && i.path.includes("size"))
  );
}

// UserSummary picks only the right fields
const summary: UserSummary = UserSummarySchema.parse(rawValidUser);
assert.equal(Object.keys(summary).sort().join(","), "active,email,id,name");

// PatchUser — only id is required; the rest are optional
const patch: PatchUser = PatchUserSchema.parse({ id: parsedUser.id, name: "Alice Updated" });
assert.equal(patch.name, "Alice Updated");
assert.equal(patch.email, undefined);

// AdminUser extends base with extra fields
const adminData = {
  ...rawValidUser,
  role: "admin" as const,
  permissions: ["read:all", "write:all"],
};
const admin: AdminUser = AdminUserSchema.parse(adminData);
assert.equal(admin.role, "admin");
assert.deepEqual(admin.permissions, ["read:all", "write:all"]);

// .strict() rejects extra keys
const StrictAddress = AddressSchema.strict();
assert.throws(() =>
  StrictAddress.parse({ street: "1 A", city: "B", state: "CA", zip: "90001", extraKey: true })
);

console.log("All tests passed!");
