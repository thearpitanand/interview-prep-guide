/**
 * Day 5 — Exercise 03: Unions and Discriminated Unions
 *
 * Define a discriminated union for an Event type using z.discriminatedUnion.
 * Write a typed handler that switches on the "kind" discriminant.
 * Verify that invalid events and missing discriminants are rejected.
 *
 * Run: npx tsx day5-runtime-validation-zod/exercises/03_unions_and_discriminated.ts
 */
import { z } from "zod";
import assert from "node:assert/strict";

// ---------- DISCRIMINATED UNION SCHEMA ----------

// TODO: define EventSchema as a z.discriminatedUnion on "kind" with these variants:
//   - "click": x (number), y (number), button (enum "left"|"right"|"middle", default "left")
//   - "keypress": key (string min 1), modifiers (array of enum "ctrl"|"alt"|"shift"|"meta", default [])
//   - "scroll": delta (number), axis (enum "vertical"|"horizontal", default "vertical")
//   - "resize": width (positive number), height (positive number)
//   - "focus": target (string), focused (boolean)
export const EventSchema = z.unknown();

type Event = z.infer<typeof EventSchema>;
// TypeScript narrows to the correct variant in switch/case blocks

// ---------- HANDLER ----------

// TODO: implement handleEvent — switch on event.kind and return a descriptive string:
//   click   → "click at (x, y) with <button> button"
//   keypress → "keypress: <key> [<modifiers joined with +>]"
//   scroll  → "scroll <axis> by <delta>"
//   resize  → "resize to <width>x<height>"
//   focus   → "<"focused"|"blurred"> on <target>"
function handleEvent(event: Event): string {
  throw new Error("TODO: implement handleEvent");
}

// ---------- GENERIC UNION for comparison ----------

// TODO: define StringOrBool as z.union of string and boolean
export const StringOrBool = z.unknown();
type StringOrBool = z.infer<typeof StringOrBool>;

// ---------- TESTS ----------

// Parse three event variants
const clickRaw = { kind: "click", x: 100, y: 200 };
const keypressRaw = { kind: "keypress", key: "Enter", modifiers: ["ctrl"] };
const scrollRaw = { kind: "scroll", delta: -120 };

const click = EventSchema.parse(clickRaw);
const keypress = EventSchema.parse(keypressRaw);
const scroll = EventSchema.parse(scrollRaw);

// Defaults applied
assert.equal(click.kind, "click");
if (click.kind === "click") {
  assert.equal(click.button, "left"); // default
}
assert.equal(keypress.kind, "keypress");
if (keypress.kind === "keypress") {
  assert.deepEqual(keypress.modifiers, ["ctrl"]);
}
assert.equal(scroll.kind, "scroll");
if (scroll.kind === "scroll") {
  assert.equal(scroll.axis, "vertical"); // default
}

// Handler produces correct strings
assert.equal(handleEvent(click), "click at (100, 200) with left button");
assert.equal(handleEvent(keypress), "keypress: Enter [ctrl]");
assert.equal(handleEvent(scroll), "scroll vertical by -120");

// Resize and focus
const resize = EventSchema.parse({ kind: "resize", width: 1920, height: 1080 });
assert.equal(handleEvent(resize), "resize to 1920x1080");

const focus = EventSchema.parse({ kind: "focus", target: "#search", focused: true });
assert.equal(handleEvent(focus), "focused on #search");

// Invalid kind — not in the union
const r1 = EventSchema.safeParse({ kind: "hover", x: 50, y: 50 });
assert.equal(r1.success, false);

// Missing discriminant field
const r2 = EventSchema.safeParse({ x: 10, y: 20 });
assert.equal(r2.success, false);

// Valid kind but wrong field types
const r3 = EventSchema.safeParse({ kind: "click", x: "not-a-number", y: 0 });
assert.equal(r3.success, false);
if (!r3.success) {
  // Error path should mention "x"
  assert.ok(r3.error.issues.some((i) => i.path.includes("x")));
}

// Generic union
const sob1: StringOrBool = StringOrBool.parse("hello");
const sob2: StringOrBool = StringOrBool.parse(false);
assert.equal(sob1, "hello");
assert.equal(sob2, false);
assert.throws(() => StringOrBool.parse(42));

// safeParse gives discriminant error on invalid kind
const r4 = EventSchema.safeParse({ kind: "dragstart", x: 1 });
assert.equal(r4.success, false);
if (!r4.success) {
  assert.ok(r4.error.issues.length > 0);
}

console.log("All tests passed!");
