/**
 * Exercise 05 — Template Literal Types
 *
 * Topics:
 *   - Deriving event handler names with `on${Capitalize<E>}`
 *   - Constraining URL paths to start with "/"
 *   - Intrinsic string manipulation types: Capitalize, Uppercase, Lowercase
 */

import assert from "node:assert/strict";

// ── Derive handler names from event names ──────────────────────────────────

type DomEvent = "click" | "focus" | "blur" | "change";
type HandlerName = `on${Capitalize<DomEvent>}`;
// "onClick" | "onFocus" | "onBlur" | "onChange"

// A record of handlers keyed by the derived names.
type HandlerMap = Partial<Record<HandlerName, () => void>>;

function attachHandlers(element: string, handlers: HandlerMap): string[] {
  return Object.keys(handlers).map((k) => `${element}: ${k}`);
}

// ── Path type that requires a leading slash ────────────────────────────────

type Path = `/${string}`;

function createUrl(base: string, path: Path): string {
  return `${base}${path}`;
}

// ── HTTP header name — conventionally Title-Case ───────────────────────────

type HttpHeaderName = `X-${Capitalize<string>}`;

function makeCustomHeader(name: string, value: string): Record<HttpHeaderName, string> {
  const key = `X-${name.charAt(0).toUpperCase()}${name.slice(1)}` as HttpHeaderName;
  return { [key]: value } as Record<HttpHeaderName, string>;
}

// ── Uppercase/Lowercase intrinsics ─────────────────────────────────────────

type EnvKey = Uppercase<"database_url" | "api_key" | "port">;
// "DATABASE_URL" | "API_KEY" | "PORT"

function getEnv(key: EnvKey): string | undefined {
  return process.env[key];
}

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
