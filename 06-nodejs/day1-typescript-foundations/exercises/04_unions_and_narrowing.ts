/**
 * Day 1 — Exercise 04: Unions and Narrowing
 *
 * Use typeof, truthiness, and in narrowing to safely operate on union types.
 * Demonstrates narrowing flows that the compiler tracks statically.
 *
 * Run: npx tsx day1-typescript-foundations/exercises/04_unions_and_narrowing.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

// --- typeof narrowing ---

// Formats a value that might be a number (raw amount) or a string (pre-formatted)
function formatAmount(value: string | number): string {
  if (typeof value === "string") {
    // value is string in this branch
    return value.trim();
  }
  // value is number in this branch
  return value >= 0
    ? `+${value.toFixed(2)}`
    : `-${Math.abs(value).toFixed(2)}`;
}

// --- truthiness narrowing ---

interface User {
  id: string;
  email: string;
  displayName?: string;
}

// Returns a greeting, safely handling the null case
function greetUser(user: User | null): string {
  if (!user) {
    // user is null here
    return "Hello, guest!";
  }
  // user is User here
  const name = user.displayName ?? user.email;
  return `Hello, ${name}!`;
}

// Also useful for optional fields
function getUserLabel(user: User): string {
  // user.displayName is string | undefined
  if (user.displayName) {
    return user.displayName;
  }
  return user.email;
}

// --- in narrowing ---

type EmailContact = { kind: "email"; address: string };
type SmsContact = { kind: "sms"; phone: string };
type Contact = EmailContact | SmsContact;

// Narrow by checking for a property that only one branch has
function describeContact(contact: Contact): string {
  if ("address" in contact) {
    // contact is EmailContact
    return `Email: ${contact.address}`;
  }
  // contact is SmsContact
  return `SMS: ${contact.phone}`;
}

// Narrow by the discriminant literal value (equivalent, often clearer)
function notifyContact(contact: Contact): string {
  if (contact.kind === "email") {
    return `Sending email to ${contact.address}`;
  }
  return `Sending SMS to ${contact.phone}`;
}

// --- combining narrowing in a realistic shape ---

type TransactionSource =
  | { channel: "api"; apiKey: string }
  | { channel: "csv"; filename: string }
  | { channel: "manual"; enteredBy: string };

function describeSource(source: TransactionSource): string {
  switch (source.channel) {
    case "api":
      return `API import (key: ${source.apiKey.slice(0, 4)}...)`;
    case "csv":
      return `CSV import from ${source.filename}`;
    case "manual":
      return `Manual entry by ${source.enteredBy}`;
  }
}

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
