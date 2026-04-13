/**
 * Day 5 — Exercise 01: Zod Basics
 *
 * Build schemas for primitive types, exercise parse and safeParse,
 * derive TypeScript types with z.infer, and explore the rich set of
 * built-in string / number / boolean refinements Zod provides.
 *
 * Run: npx tsx day5-runtime-validation-zod/exercises/01_zod_basics.ts
 */
import { z } from "zod";
import assert from "node:assert/strict";

// ---------- PRIMITIVE SCHEMAS ----------

// A simple string schema
const NameSchema = z.string().min(1).max(100);
type Name = z.infer<typeof NameSchema>;

// Number with bounds
const AgeSchema = z.number().int().min(0).max(150);
type Age = z.infer<typeof AgeSchema>;

// Boolean
const ActiveSchema = z.boolean();
type Active = z.infer<typeof ActiveSchema>;

// Literal — only the exact value passes
const AdminLiteralSchema = z.literal("admin");
type AdminLiteral = z.infer<typeof AdminLiteralSchema>;

// Enum — one of several string values
const RoleSchema = z.enum(["admin", "user", "moderator"]);
type Role = z.infer<typeof RoleSchema>;

// ---------- STRING REFINEMENTS ----------

const EmailSchema = z.string().email();
const UrlSchema = z.string().url();
const UuidSchema = z.string().uuid();
const ZipSchema = z.string().regex(/^\d{5}(-\d{4})?$/, "Invalid US ZIP code");
const PasswordSchema = z
  .string()
  .min(8, "Password must be at least 8 characters")
  .refine((s) => /[A-Z]/.test(s), "Must contain at least one uppercase letter")
  .refine((s) => /\d/.test(s), "Must contain at least one digit");

// ---------- PARSE: throws on invalid input ----------

// .parse returns the validated value directly
const validName: Name = NameSchema.parse("Alice");
const validAge: Age = AgeSchema.parse(30);
const validActive: Active = ActiveSchema.parse(true);
const validRole: Role = RoleSchema.parse("admin");

// ---------- SAFEPARSE: returns a result object ----------

// Happy path
const successResult = EmailSchema.safeParse("user@example.com");
// Failure path
const failureResult = EmailSchema.safeParse("not-an-email");

// ---------- TESTS ----------

// Primitive parses
assert.equal(validName, "Alice");
assert.equal(validAge, 30);
assert.equal(validActive, true);
assert.equal(validRole, "admin");

// safeParse success shape
assert.equal(successResult.success, true);
if (successResult.success) {
  assert.equal(successResult.data, "user@example.com");
}

// safeParse failure shape
assert.equal(failureResult.success, false);
if (!failureResult.success) {
  assert.ok(failureResult.error.issues.length > 0);
  assert.ok(
    failureResult.error.issues.some((i) =>
      i.message.toLowerCase().includes("email")
    )
  );
}

// String refinements — valid
assert.doesNotThrow(() => EmailSchema.parse("hello@world.io"));
assert.doesNotThrow(() => UrlSchema.parse("https://example.com/path?q=1"));
assert.doesNotThrow(() => UuidSchema.parse("550e8400-e29b-41d4-a716-446655440000"));
assert.doesNotThrow(() => ZipSchema.parse("90210"));
assert.doesNotThrow(() => ZipSchema.parse("10001-1234"));
assert.doesNotThrow(() =>
  PasswordSchema.parse("SecurePass1")
);

// String refinements — invalid
assert.throws(() => EmailSchema.parse("no-at-sign"));
assert.throws(() => UrlSchema.parse("not a url"));
assert.throws(() => UuidSchema.parse("not-a-uuid"));
assert.throws(() => ZipSchema.parse("ABCDE"));
assert.throws(() => PasswordSchema.parse("short")); // too short
assert.throws(() => PasswordSchema.parse("alllowercase1")); // no uppercase
assert.throws(() => PasswordSchema.parse("NoDigitsHere")); // no digit

// Number refinements
assert.doesNotThrow(() => z.number().int().min(0).max(10).parse(5));
assert.throws(() => z.number().int().parse(3.14));
assert.throws(() => z.number().positive().parse(0));
assert.throws(() => z.number().max(100).parse(101));

// Literal
assert.doesNotThrow(() => AdminLiteralSchema.parse("admin"));
assert.throws(() => AdminLiteralSchema.parse("user"));

// Enum — .enum property gives the enum map
assert.equal(RoleSchema.enum.admin, "admin");
assert.equal(RoleSchema.enum.moderator, "moderator");
assert.throws(() => RoleSchema.parse("superuser"));

// z.infer extracts the correct types (verified statically, shown here as runtime checks)
const nameValue: Name = "Bob"; // string
const ageValue: Age = 25;      // number
assert.equal(typeof nameValue, "string");
assert.equal(typeof ageValue, "number");

console.log("All tests passed!");
