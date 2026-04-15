/**
 * Day 1 — Exercise 04: Unions and Narrowing
 *
 * Use typeof, truthiness, and in narrowing to safely operate on union types.
 * Demonstrates narrowing flows that the compiler tracks statically.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/04_unions_and_narrowing.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - function formatAmount(value: string | number): string
//       — if string: return value.trim()
//       — if number: positive → "+X.XX", negative → "-X.XX" (no sign for original)
//   - interface User                              — id: string, email: string, displayName?: string
//   - function greetUser(user: User | null): string
//       — null → "Hello, guest!"
//       — User → "Hello, <displayName or email>!"
//   - function getUserLabel(user: User): string   — displayName if truthy, else email
//   - type EmailContact                           — { kind: "email"; address: string }
//   - type SmsContact                             — { kind: "sms"; phone: string }
//   - type Contact                               — EmailContact | SmsContact
//   - function describeContact(contact: Contact): string
//       — narrow by "address" in contact: "Email: <address>" or "SMS: <phone>"
//   - function notifyContact(contact: Contact): string
//       — narrow by contact.kind: "Sending email to <address>" or "Sending SMS to <phone>"
//   - type TransactionSource                      — discriminated union on channel:
//       "api" (apiKey), "csv" (filename), "manual" (enteredBy)
//   - function describeSource(source: TransactionSource): string
//       — switch on channel: see test assertions for exact output format
// Read the tests to infer expected values.

// ---------- TESTS ----------

// typeof narrowing — string path
assert.equal(formatAmount("  $42.00  "), "$42.00");

// typeof narrowing — number path, positive
assert.equal(formatAmount(123.5), "+123.50");

// typeof narrowing — number path, negative
assert.equal(formatAmount(-45.75), "-45.75");

// truthiness narrowing — null path
assert.equal(greetUser(null), "Hello, guest!");

// truthiness narrowing — User path with displayName
assert.equal(
  greetUser({ id: "u1", email: "a@b.com", displayName: "Alice", createdAt: new Date() } as User & { createdAt: Date }),
  "Hello, Alice!"
);

// truthiness narrowing — User path without displayName (falls back to email)
assert.equal(
  greetUser({ id: "u2", email: "b@c.com" }),
  "Hello, b@c.com!"
);

// getUserLabel: uses displayName when present
assert.equal(getUserLabel({ id: "u1", email: "a@b.com", displayName: "Alice" }), "Alice");

// getUserLabel: falls back to email
assert.equal(getUserLabel({ id: "u2", email: "b@c.com" }), "b@c.com");

// in narrowing — email branch
const emailContact: Contact = { kind: "email", address: "hi@example.com" };
assert.equal(describeContact(emailContact), "Email: hi@example.com");

// in narrowing — sms branch
const smsContact: Contact = { kind: "sms", phone: "+15551234567" };
assert.equal(describeContact(smsContact), "SMS: +15551234567");

// discriminant narrowing
assert.equal(notifyContact(emailContact), "Sending email to hi@example.com");
assert.equal(notifyContact(smsContact), "Sending SMS to +15551234567");

// switch on discriminant literal
assert.equal(
  describeSource({ channel: "api", apiKey: "sk-abcdef" }),
  "API import (key: sk-a...)"
);
assert.equal(
  describeSource({ channel: "csv", filename: "transactions_q1.csv" }),
  "CSV import from transactions_q1.csv"
);
assert.equal(
  describeSource({ channel: "manual", enteredBy: "Bob" }),
  "Manual entry by Bob"
);

console.log("All tests passed!");
