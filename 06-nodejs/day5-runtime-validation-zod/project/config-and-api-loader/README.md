# Config and API Loader

## Run

```bash
npx tsx day5-runtime-validation-zod/project/config-and-api-loader/src/index.ts
```

## What It Does

A CLI that loads JSON from three sources, validates each with Zod, and prints a clean typed summary. Invalid records are shown with human-readable error output so you can see Zod's error reporting on real data.

## Input Sources

### 1. `data/config.json`

A nested application config object with database, server, feature-flag, and logging sections. All fields are valid. The `ConfigSchema` validates required keys and coerces numeric strings where needed.

### 2. `data/users.json`

An array of ~10 user records. Three of them are deliberately invalid:
- One is missing a required field (`email`)
- One has the wrong type (`age` is a string instead of a number)
- One has an invalid email format

The loader uses `safeParse` per record so all errors are collected — not just the first.

### 3. `data/api_response.json`

A simulated API response using a discriminated union (`"status": "success" | "error"`). The success variant contains an array of typed `ApiResult` records. The loader validates the wrapper and the nested results.

## Target Schemas

Defined in `src/schemas.ts`:

| Schema | Description |
|--------|-------------|
| `ConfigSchema` | Nested app config (db, server, features, logging) |
| `UserSchema` | User record with email, age, role, address |
| `ApiResponseSchema` | Discriminated union: success variant wraps `ApiResult[]` |

All TypeScript types are derived via `z.infer` — no separate interfaces.

## Expected Output

```
=== Config ===
Loaded: 1 valid, 0 invalid

=== Users ===
Loaded: 7 valid, 3 invalid

Invalid record #2:
  email: Invalid email
Invalid record #4:
  age: Expected number, received string
Invalid record #8:
  name: Required

=== API Response ===
Status: success
Results: 4 records loaded

=== Summary ===
Total valid:   12
Total invalid: 3
```

## Acceptance Checklist

- [ ] Running the command above prints the summary without crashing
- [ ] Config loads with no validation errors
- [ ] Exactly 3 user records fail with readable, field-level error messages
- [ ] API response is parsed as a success variant with typed results
- [ ] No TypeScript `any` — all types derived from schemas
- [ ] Invalid records do not prevent valid ones from loading
