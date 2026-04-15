/**
 * Exercise 05 — Template Literal Types
 *
 * Topics:
 *   - Deriving event handler names with `on${Capitalize<E>}`
 *   - Constraining URL paths to start with "/"
 *   - Intrinsic string manipulation types: Capitalize, Uppercase, Lowercase
 */

import assert from "node:assert/strict";

// ---------- YOUR CODE BELOW ----------
// TODO: Declare the following so that the tests below pass.
//   - DomEvent: union literal type "click" | "focus" | "blur" | "change"
//   - HandlerName: template literal type deriving "onClick" | "onFocus" | "onBlur" | "onChange"
//   - HandlerMap: Partial<Record<HandlerName, () => void>>
//   - attachHandlers(element: string, handlers: HandlerMap): string[]
//       returns an array of "<element>: <handlerKey>" strings for each key in handlers
//   - Path: template literal type constraining strings to start with "/"
//   - createUrl(base: string, path: Path): string — concatenates base + path
//   - HttpHeaderName: template literal type `X-${Capitalize<string>}`
//   - makeCustomHeader(name: string, value: string): Record<HttpHeaderName, string>
//       capitalizes the first letter of name and returns { "X-<Name>": value }
//   - EnvKey: Uppercase<"database_url" | "api_key" | "port">
//       i.e. "DATABASE_URL" | "API_KEY" | "PORT"
//   - getEnv(key: EnvKey): string | undefined — returns process.env[key]

// ── Tests ─────────────────────────────────────────────────────────────────

// Handler names are correctly derived at the type level.
const handlers: HandlerMap = {
  onClick: () => {},
  onFocus: () => {},
};
const attached = attachHandlers("button", handlers);
assert.equal(attached.length, 2);
assert.ok(attached.some((s) => s.includes("onClick")));
assert.ok(attached.some((s) => s.includes("onFocus")));

// createUrl works with a valid path.
assert.equal(createUrl("https://api.example.com", "/users"), "https://api.example.com/users");
assert.equal(createUrl("https://api.example.com", "/users/42"), "https://api.example.com/users/42");

// makeCustomHeader produces the right key.
const header = makeCustomHeader("requestId", "abc-123");
assert.equal(header["X-RequestId"], "abc-123");

// getEnv returns undefined for a key that's not set (fine — we just check it runs).
const val = getEnv("DATABASE_URL");
assert.ok(val === undefined || typeof val === "string");

console.log("All tests passed!");
