/**
 * Day 5 — Exercise 06: Schema Composition
 *
 * Build a base EntitySchema (id + timestamps) and extend it for
 * UserSchema and ProductSchema. Create DTOs via .pick/.omit.
 * Use .merge for mixin-style composition.
 *
 * Run: npx tsx day5-runtime-validation-zod/exercises/06_schema_composition.ts
 */
import { z } from "zod";
import assert from "node:assert/strict";

// ---------- BASE SCHEMA ----------

// Every entity in our system has these fields
const EntitySchema = z.object({
  id: z.string().uuid(),
  createdAt: z.coerce.date(), // coerce so ISO strings work
  updatedAt: z.coerce.date(),
});

type Entity = z.infer<typeof EntitySchema>;

// ---------- MIXIN: soft-delete support ----------

const SoftDeletableSchema = z.object({
  deletedAt: z.coerce.date().nullable().default(null),
});

// ---------- USER SCHEMA — extends Entity ----------

const UserSchema = EntitySchema.extend({
  email: z.string().email(),
  name: z.string().min(1),
  role: z.enum(["admin", "user", "moderator"]),
  bio: z.string().max(500).optional(),
}).merge(SoftDeletableSchema);

type User = z.infer<typeof UserSchema>;

// ---------- PRODUCT SCHEMA — extends Entity ----------

const ProductSchema = EntitySchema.extend({
  name: z.string().min(1),
  description: z.string().max(2000).optional(),
  price: z.number().positive(),
  currency: z.string().length(3).default("USD"), // ISO 4217
  category: z.enum(["electronics", "clothing", "food", "books", "other"]),
  inStock: z.boolean().default(true),
  tags: z.array(z.string()).default([]),
}).merge(SoftDeletableSchema);

type Product = z.infer<typeof ProductSchema>;

// ---------- DTOs ----------

// What the API returns when listing users — no sensitive timestamps
const UserListItemSchema = UserSchema.pick({
  id: true,
  email: true,
  name: true,
  role: true,
});
type UserListItem = z.infer<typeof UserListItemSchema>;

// What the client sends to create a user — no id, timestamps, or deletedAt
const CreateUserSchema = UserSchema.omit({
  id: true,
  createdAt: true,
  updatedAt: true,
  deletedAt: true,
});
type CreateUser = z.infer<typeof CreateUserSchema>;

// PATCH schema — all fields optional except id
const PatchUserSchema = UserSchema.partial().required({ id: true });
type PatchUser = z.infer<typeof PatchUserSchema>;

// Product summary DTO
const ProductSummarySchema = ProductSchema.pick({
  id: true,
  name: true,
  price: true,
  currency: true,
  inStock: true,
  category: true,
});
type ProductSummary = z.infer<typeof ProductSummarySchema>;

// ---------- COMPOSITION WITH .merge ----------

// AuditedSchema adds audit fields to any schema
const AuditFieldsSchema = z.object({
  createdBy: z.string().uuid(),
  updatedBy: z.string().uuid().optional(),
});

// Extend a DTO with audit fields via .merge
const AuditedUserSchema = UserListItemSchema.merge(AuditFieldsSchema);
type AuditedUser = z.infer<typeof AuditedUserSchema>;

// ---------- TEST DATA ----------

const now = new Date();
const uuid1 = "550e8400-e29b-41d4-a716-446655440000";
const uuid2 = "550e8400-e29b-41d4-a716-446655440001";
const uuid3 = "550e8400-e29b-41d4-a716-446655440002";

const rawUser = {
  id: uuid1,
  email: "alice@example.com",
  name: "Alice Smith",
  role: "admin",
  createdAt: now.toISOString(),
  updatedAt: now.toISOString(),
};

const rawProduct = {
  id: uuid2,
  name: "Mechanical Keyboard",
  price: 149.99,
  category: "electronics",
  createdAt: now.toISOString(),
  updatedAt: now.toISOString(),
};

// ---------- TESTS ----------

// EntitySchema base
const entity: Entity = EntitySchema.parse({
  id: uuid1,
  createdAt: now.toISOString(),
  updatedAt: now.toISOString(),
});
assert.ok(entity.createdAt instanceof Date);

// UserSchema — dates coerced from strings, deletedAt defaults to null
const user: User = UserSchema.parse(rawUser);
assert.equal(user.id, uuid1);
assert.equal(user.email, "alice@example.com");
assert.equal(user.role, "admin");
assert.equal(user.deletedAt, null); // default applied
assert.ok(user.createdAt instanceof Date);

// ProductSchema — defaults applied
const product: Product = ProductSchema.parse(rawProduct);
assert.equal(product.currency, "USD"); // default
assert.equal(product.inStock, true); // default
assert.deepEqual(product.tags, []); // default
assert.equal(product.deletedAt, null);

// UserListItem DTO — only picked fields
const listItem: UserListItem = UserListItemSchema.parse(rawUser);
const listItemKeys = Object.keys(listItem).sort();
assert.deepEqual(listItemKeys, ["email", "id", "name", "role"]);

// CreateUser DTO — no id/timestamps
const createInput: CreateUser = CreateUserSchema.parse({
  email: "bob@example.com",
  name: "Bob",
  role: "user",
});
assert.equal("id" in createInput, false);
assert.equal("createdAt" in createInput, false);

// PatchUser — only id is required
const patch: PatchUser = PatchUserSchema.parse({ id: uuid1, name: "Alice Updated" });
assert.equal(patch.id, uuid1);
assert.equal(patch.name, "Alice Updated");
assert.equal(patch.email, undefined);

// ProductSummary DTO
const summary: ProductSummary = ProductSummarySchema.parse(rawProduct);
assert.equal(summary.name, "Mechanical Keyboard");
assert.equal(summary.price, 149.99);
assert.equal("description" in summary, false); // not in pick

// AuditedUser — merge adds audit fields
const auditedUser: AuditedUser = AuditedUserSchema.parse({
  id: uuid1,
  email: "alice@example.com",
  name: "Alice",
  role: "admin",
  createdBy: uuid3,
});
assert.equal(auditedUser.createdBy, uuid3);
assert.equal(auditedUser.updatedBy, undefined);

// Invalid product — negative price
const r1 = ProductSchema.safeParse({ ...rawProduct, price: -5 });
assert.equal(r1.success, false);
if (!r1.success) {
  assert.ok(r1.error.issues.some((i) => i.path.includes("price")));
}

// Invalid user role
const r2 = UserSchema.safeParse({ ...rawUser, role: "superadmin" });
assert.equal(r2.success, false);

// Inheritance chain preserves all fields
assert.equal(typeof user.bio, "undefined"); // optional, not present
const userWithBio: User = UserSchema.parse({ ...rawUser, bio: "Software engineer" });
assert.equal(userWithBio.bio, "Software engineer");

console.log("All tests passed!");
