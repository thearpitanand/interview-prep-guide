# Project: In-Memory Table

**Run:**

```bash
npx tsx day2-generics-and-utility-types/project/in-memory-table/src/index.ts
```

## What It Is

`Table<T>` is a generic, type-safe in-memory store modelled on a lightweight relational table. It supports typed CRUD operations and basic query primitives.

`T` must extend `{ id: string }` — every record needs a primary key.

## API

| Method | Signature | Description |
|--------|-----------|-------------|
| `insert` | `insert(record: T): T` | Add a record. Throws if the id already exists. |
| `findById` | `findById(id: string): T \| undefined` | Look up by primary key. |
| `update` | `update(id: string, patch: Partial<Omit<T, "id">>): T` | Merge patch fields into an existing record. Returns the updated record. Throws if not found. |
| `delete` | `delete(id: string): boolean` | Remove a record. Returns `true` if it existed, `false` otherwise. |
| `where` | `where(predicate: (record: T) => boolean): T[]` | Filter all records. |
| `pluck` | `pluck<K extends keyof T>(key: K): T[K][]` | Return an array of a single field from all records. |
| `groupBy` | `groupBy<K extends keyof T>(key: K): Record<string, T[]>` | Group all records by the value of a field. |
| `count` | `count(): number` | Total number of records. |
| `all` | `all(): T[]` | Return all records as an array. |

## Acceptance Checklist

- [ ] `insert` adds a record retrievable by `findById`
- [ ] `update` merges only the provided fields; other fields are unchanged
- [ ] `delete` removes the record; subsequent `findById` returns `undefined`
- [ ] `where` returns only records matching the predicate
- [ ] `pluck("email")` returns a `string[]` (typed to the field type, not `unknown[]`)
- [ ] `groupBy("role")` returns `Record<string, User[]>` — all records grouped
- [ ] `groupBy("nope")` would be a TypeScript compile error (key must be `keyof T`)
- [ ] `count()` reflects inserts and deletes accurately
- [ ] The driver in `src/index.ts` runs without errors and prints query results
