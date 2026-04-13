# Setup Guide — 06-nodejs

This course uses one shared `package.json` and one shared `tsconfig.json` at the root of `06-nodejs/`. You install dependencies **once** and every day's exercises and project can use them.

---

## 1. Prerequisites

| Tool | Minimum Version | Check with | Install |
|------|-----------------|------------|---------|
| Node.js | 20.x (LTS) | `node --version` | [nodejs.org](https://nodejs.org) or `brew install node` |
| npm | 10.x | `npm --version` | ships with Node |

> Why Node 20+? We use native `node:test`, `node --test`, `fetch`, `AbortSignal`, and modern stream APIs. Older Node versions will fail on day 6 (streams) and day 7 (capstone tests).

---

## 2. One-time install

```bash
cd 06-nodejs
npm install
```

This installs:

| Package | Purpose | First used |
|---------|---------|-----------|
| `typescript` | the compiler | day 1 |
| `tsx` | run `.ts` files directly, no build step | day 1 |
| `@types/node` | type definitions for the Node standard library | day 1 |
| `zod` | runtime schema validation | day 5 |
| `csv-parse` | streaming CSV parser | day 6 |
| `csv-stringify` | streaming CSV writer | day 6 |

No other installs are required for the rest of the course.

---

## 3. How to run things

### Run any exercise file

From the `06-nodejs/` directory:

```bash
npx tsx day1-typescript-foundations/exercises/01_primitives_and_inference.ts
```

A passing file ends with `All tests passed!`. A failing assertion will throw an `AssertionError` with a line number — read the stack trace, fix the code, run it again.

### Run a day's project

Every project has a `README.md` with a **run command** at the top. Usually:

```bash
npx tsx day4-nested-data-transformations/project/orders-to-csv/src/index.ts
```

### Type-check without running

```bash
npx tsc --noEmit
```

This runs the compiler against the whole course in check-only mode. Useful before committing — if this passes, your types are sound even for files you haven't run yet.

### Run day 7 capstone tests

```bash
cd day7-capstone-data-toolkit/project/data-toolkit-cli
npx tsx --test tests/*.test.ts
```

---

## 4. Editor setup

### VS Code (recommended)

Open the `06-nodejs/` folder as the workspace root (not the whole repo) — this way VS Code picks up the `tsconfig.json` and you get accurate IntelliSense on every exercise file.

Useful extensions:
- **ESLint** — optional, not required by the course
- **Error Lens** — shows type errors inline, huge quality-of-life for a beginner
- **vscode-icons** — just makes the file tree easier to scan

Settings you may want in `.vscode/settings.json` (create if missing):

```json
{
  "typescript.tsdk": "node_modules/typescript/lib",
  "typescript.enablePromptUseWorkspaceTsdk": true,
  "editor.formatOnSave": true
}
```

### JetBrains / WebStorm

Right-click `tsconfig.json` → **Use TypeScript Service**. WebStorm will auto-detect.

---

## 5. The assertion convention

Every exercise file imports from `node:assert/strict`:

```ts
import assert from "node:assert/strict";

// ... your code ...

assert.equal(result, expected);
console.log("All tests passed!");
```

This matches the DSA pillar's Python convention (`assert` + final print). No test framework ceremony, no describe/it blocks, no config. A file either runs cleanly to the final `console.log` or it throws.

---

## 6. Strict mode — what you've signed up for

The `tsconfig.json` has `strict: true` **and** `noUncheckedIndexedAccess: true`. This is intentional and will bite you early:

```ts
const names = ["alice", "bob"];
const first = names[0];           // type: string | undefined  (not string!)
console.log(first.toUpperCase()); // ❌ TS error
```

This seems annoying at first but it's exactly the discipline that will make you handle messy real-world data safely. Day 1 teaches you how to narrow `T | undefined` to `T`. Trust the process.

---

## 7. Troubleshooting

| Symptom | Fix |
|---------|-----|
| `command not found: tsx` | You forgot `npm install` in `06-nodejs/`. Run it. |
| `Cannot find module 'node:assert/strict'` | Your Node is < 18. Upgrade to 20 LTS. |
| `SyntaxError: Cannot use import statement outside a module` | You're running with `node` instead of `npx tsx`. Use `tsx`. |
| Red squigglies everywhere in VS Code but `tsx` runs fine | VS Code opened the wrong folder. Open `06-nodejs/` as the workspace root. |
| `npm install` downloads forever | Use `npm ci` instead if `package-lock.json` exists. |

---

## 8. Ready?

Head to [`00-README.md`](./00-README.md) for the full course overview, then open [`day1-typescript-foundations/concepts.md`](./day1-typescript-foundations/concepts.md) and start the timer.
