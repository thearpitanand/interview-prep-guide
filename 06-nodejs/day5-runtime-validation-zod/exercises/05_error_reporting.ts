/**
 * Day 5 — Exercise 05: Error Reporting
 *
 * Deliberately feed invalid data to Zod schemas and inspect the three
 * error-reporting APIs: error.issues, error.flatten(), error.format().
 * Build a helper that converts a ZodError into a human-readable summary.
 *
 * Run: npx tsx day5-runtime-validation-zod/exercises/05_error_reporting.ts
 */
import { z } from "zod";
import assert from "node:assert/strict";

// ---------- SCHEMA ----------

const AddressSchema = z.object({
  street: z.string().min(1),
  city: z.string().min(1),
  zip: z.string().regex(/^\d{5}$/, "ZIP must be exactly 5 digits"),
});

const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(2, "Name must be at least 2 characters"),
  age: z.number().int().min(0).max(150),
  role: z.enum(["admin", "user", "moderator"]),
  address: AddressSchema,
});

type User = z.infer<typeof UserSchema>;

// ---------- HELPERS ----------

// Produce a human-friendly per-field error summary from .flatten()
function formatFlatErrors(error: z.ZodError): string {
  const flat = error.flatten();
  const lines: string[] = [];

  if (flat.formErrors.length > 0) {
    lines.push(`Form errors: ${flat.formErrors.join(", ")}`);
  }

  for (const [field, msgs] of Object.entries(flat.fieldErrors)) {
    if (msgs && msgs.length > 0) {
      lines.push(`  ${field}: ${msgs.join(", ")}`);
    }
  }

  return lines.length > 0 ? lines.join("\n") : "No errors";
}

// Produce a nested summary from .format() — walks the formatted tree
function formatNestedErrors(
  formatted: z.ZodFormattedError<unknown>,
  prefix = ""
): string[] {
  const lines: string[] = [];
  const obj = formatted as Record<string, unknown>;

  for (const [key, val] of Object.entries(obj)) {
    if (key === "_errors") {
      const errs = val as string[];
      if (errs.length > 0) {
        lines.push(`${prefix || "root"}: ${errs.join(", ")}`);
      }
    } else if (typeof val === "object" && val !== null) {
      lines.push(
        ...formatNestedErrors(
          val as z.ZodFormattedError<unknown>,
          prefix ? `${prefix}.${key}` : key
        )
      );
    }
  }

  return lines;
}

// ---------- TEST DATA — all invalid ----------

const multipleErrors = {
  id: "not-a-uuid",
  email: "bad-email",
  name: "X",         // too short
  age: 200,          // over max
  role: "superuser", // not in enum
  address: {
    street: "",      // too short
    city: "Austin",
    zip: "ABCDE",    // not digits
  },
};

const missingFields = {
  // id missing
  email: "alice@example.com",
  // name missing
  age: 30,
  role: "user",
  address: {
    street: "123 Main",
    city: "Chicago",
    zip: "60601",
  },
};

// ---------- TESTS ----------

// multipleErrors — collect all issues
const r1 = UserSchema.safeParse(multipleErrors);
assert.equal(r1.success, false);

if (!r1.success) {
  // error.issues is the raw array
  assert.ok(r1.error.issues.length >= 5, `Expected at least 5 issues, got ${r1.error.issues.length}`);

  // Verify specific paths are present
  const paths = r1.error.issues.map((i) => i.path.join("."));
  assert.ok(paths.includes("id"), "Should have id error");
  assert.ok(paths.includes("email"), "Should have email error");
  assert.ok(paths.includes("name"), "Should have name error");
  assert.ok(paths.includes("age"), "Should have age error");
  assert.ok(paths.includes("role"), "Should have role error");

  // nested path
  assert.ok(
    paths.some((p) => p.startsWith("address")),
    "Should have address error"
  );

  // error.flatten()
  const flat = r1.error.flatten();
  assert.equal(Array.isArray(flat.formErrors), true);
  assert.ok(flat.fieldErrors["id"] !== undefined);
  assert.ok(flat.fieldErrors["email"] !== undefined);

  // error.format()
  const formatted = r1.error.format();
  // The formatted object has nested structure
  assert.ok(typeof formatted === "object");

  // Build human-readable flat summary
  const summary = formatFlatErrors(r1.error);
  assert.ok(summary.includes("email"));
  assert.ok(summary.includes("id"));

  // Build nested summary from format()
  const nestedLines = formatNestedErrors(formatted);
  assert.ok(nestedLines.length > 0);
  // Address.zip or address.street should appear
  assert.ok(
    nestedLines.some((l) => l.includes("address")),
    "Nested errors should mention address"
  );
}

// missingFields — required field errors
const r2 = UserSchema.safeParse(missingFields);
assert.equal(r2.success, false);

if (!r2.success) {
  const flat = r2.error.flatten();
  // id and name are required and missing
  assert.ok(flat.fieldErrors["id"] !== undefined, "id should be required");
  assert.ok(flat.fieldErrors["name"] !== undefined, "name should be required");

  // issues array should have "invalid_type" codes for missing fields
  const invalidType = r2.error.issues.filter((i) => i.code === "invalid_type");
  assert.ok(invalidType.length > 0);

  // Every issue has a message
  for (const issue of r2.error.issues) {
    assert.ok(typeof issue.message === "string" && issue.message.length > 0);
  }
}

// Show the shape of a ZodError issue
const r3 = UserSchema.safeParse({ id: "bad", email: "bad" });
if (!r3.success) {
  const issue = r3.error.issues[0];
  assert.ok(issue !== undefined);
  // Each issue has: code, path, message
  assert.ok("code" in issue);
  assert.ok("path" in issue);
  assert.ok("message" in issue);
  assert.ok(Array.isArray(issue.path));
}

// A valid parse produces no errors
const valid = UserSchema.safeParse({
  id: "550e8400-e29b-41d4-a716-446655440000",
  email: "alice@example.com",
  name: "Alice",
  age: 30,
  role: "admin",
  address: { street: "123 Main", city: "Chicago", zip: "60601" },
});
assert.equal(valid.success, true);

console.log("All tests passed!");
