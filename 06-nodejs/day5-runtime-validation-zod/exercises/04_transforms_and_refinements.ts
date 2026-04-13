/**
 * Day 5 — Exercise 04: Transforms and Refinements
 *
 * - z.preprocess: normalize a string date into a Date before validating
 * - .superRefine: cross-field validation (endDate > startDate)
 * - .transform: normalize email to lowercase, enrich an object
 * - z.coerce: type coercion from env-like strings
 *
 * Run: npx tsx day5-runtime-validation-zod/exercises/04_transforms_and_refinements.ts
 */
import { z } from "zod";
import assert from "node:assert/strict";

// ---------- PREPROCESS: string → Date before validation ----------

// z.date() requires an actual Date object — strings fail by default.
// z.preprocess runs BEFORE validation and normalizes the input.
const FlexibleDateSchema = z.preprocess(
  (val) => {
    if (typeof val === "string" || typeof val === "number") {
      const d = new Date(val);
      // Return NaN-date as-is so z.date() produces a proper error
      return d;
    }
    return val;
  },
  z.date()
);

// ---------- CROSS-FIELD REFINEMENT: endDate > startDate ----------

const DateRangeSchema = z
  .object({
    startDate: FlexibleDateSchema,
    endDate: FlexibleDateSchema,
    label: z.string().min(1),
  })
  .superRefine((data, ctx) => {
    if (data.endDate <= data.startDate) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: "endDate must be strictly after startDate",
        path: ["endDate"],
      });
    }
  });

type DateRange = z.infer<typeof DateRangeSchema>;

// ---------- TRANSFORM: normalize email ----------

// .trim() preprocesses the string before .email() validates it,
// then .transform lowercases the already-trimmed value.
const NormalizedEmailSchema = z
  .string()
  .trim()
  .email()
  .transform((s) => s.toLowerCase());

// After transform, z.infer is still string, but the value is lowercased
type NormalizedEmail = z.infer<typeof NormalizedEmailSchema>;

// ---------- TRANSFORM: enrich an object ----------

const RawScoreSchema = z.object({
  name: z.string(),
  score: z.number().min(0).max(100),
});

const EnrichedScoreSchema = RawScoreSchema.transform((data) => ({
  ...data,
  grade:
    data.score >= 90
      ? "A"
      : data.score >= 80
      ? "B"
      : data.score >= 70
      ? "C"
      : data.score >= 60
      ? "D"
      : "F",
  passed: data.score >= 60,
}));

type EnrichedScore = z.infer<typeof EnrichedScoreSchema>;

// ---------- Z.COERCE: env-style string coercion ----------

// z.coerce.number calls Number(val) then validates as number
const EnvPortSchema = z.coerce.number().int().min(1).max(65535);
// Guard against NaN (Number("abc") === NaN)
const SafeEnvPortSchema = z.coerce
  .number()
  .refine((n) => !isNaN(n), "Not a valid number")
  .pipe(z.number().int().min(1).max(65535));

// ---------- TESTS ----------

// preprocess: string → Date
const d1 = FlexibleDateSchema.parse("2024-06-15");
assert.ok(d1 instanceof Date);
assert.equal(d1.getFullYear(), 2024);

// preprocess: number → Date
const d2 = FlexibleDateSchema.parse(0);
assert.ok(d2 instanceof Date);

// preprocess: already a Date
const existing = new Date("2024-01-01");
const d3 = FlexibleDateSchema.parse(existing);
assert.deepEqual(d3, existing);

// Invalid string → ZodError
assert.throws(() => FlexibleDateSchema.parse("not-a-date"));

// DateRange — valid
const range1 = DateRangeSchema.parse({
  startDate: "2024-01-01",
  endDate: "2024-12-31",
  label: "Full year",
});
assert.ok(range1.endDate > range1.startDate);
assert.equal(range1.label, "Full year");

// DateRange — endDate before startDate
const r1 = DateRangeSchema.safeParse({
  startDate: "2024-12-31",
  endDate: "2024-01-01",
  label: "Backwards",
});
assert.equal(r1.success, false);
if (!r1.success) {
  assert.ok(r1.error.issues.some((i) => i.path.includes("endDate")));
  assert.ok(
    r1.error.issues.some((i) =>
      i.message.includes("endDate must be strictly after startDate")
    )
  );
}

// DateRange — equal dates are also rejected
const r2 = DateRangeSchema.safeParse({
  startDate: "2024-06-01",
  endDate: "2024-06-01",
  label: "Same day",
});
assert.equal(r2.success, false);

// NormalizedEmail transform
const email1: NormalizedEmail = NormalizedEmailSchema.parse("  Alice@EXAMPLE.COM  ");
assert.equal(email1, "alice@example.com");

const email2 = NormalizedEmailSchema.parse("BOB@Test.Org");
assert.equal(email2, "bob@test.org");

// Invalid email still fails before transform
assert.throws(() => NormalizedEmailSchema.parse("not-an-email"));

// EnrichedScore transform
const score1: EnrichedScore = EnrichedScoreSchema.parse({ name: "Alice", score: 95 });
assert.equal(score1.grade, "A");
assert.equal(score1.passed, true);

const score2 = EnrichedScoreSchema.parse({ name: "Bob", score: 55 });
assert.equal(score2.grade, "F");
assert.equal(score2.passed, false);

const score3 = EnrichedScoreSchema.parse({ name: "Carol", score: 73 });
assert.equal(score3.grade, "C");
assert.equal(score3.passed, true);

// z.coerce from string
const port = EnvPortSchema.parse("3000");
assert.equal(port, 3000);
assert.equal(typeof port, "number");

// z.coerce from number string
const port2 = EnvPortSchema.parse("443");
assert.equal(port2, 443);

// Out of range
assert.throws(() => EnvPortSchema.parse("0"));
assert.throws(() => EnvPortSchema.parse("99999"));

// SafeEnvPortSchema guards against NaN
const r3 = SafeEnvPortSchema.safeParse("abc");
assert.equal(r3.success, false);

console.log("All tests passed!");
