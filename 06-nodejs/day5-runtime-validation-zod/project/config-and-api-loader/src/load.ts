/**
 * load.ts — Functions that read each data source and run safeParse.
 *
 * Each loader returns:
 *   { valid: T[]; invalid: { raw: unknown; error: ZodError }[] }
 *
 * Using safeParse means a single bad record never aborts the whole batch.
 */
import { readFile } from "node:fs/promises";
import { z } from "zod";
import {
  ConfigSchema,
  UserSchema,
  ApiResponseSchema,
  type Config,
  type User,
  type ApiResponse,
} from "./schemas.ts";

// Generic result type returned by every loader
export type LoadResult<T> = {
  valid: T[];
  invalid: { raw: unknown; error: z.ZodError }[];
};

// ---------- HELPERS ----------

async function readJson(filePath: string): Promise<unknown> {
  const text = await readFile(filePath, "utf-8");
  return JSON.parse(text) as unknown;
}

// ---------- CONFIG LOADER ----------
// Config is a single object, not an array — either it parses or it doesn't.

export async function loadConfig(filePath: string): Promise<LoadResult<Config>> {
  const raw = await readJson(filePath);
  const result = ConfigSchema.safeParse(raw);

  if (result.success) {
    return { valid: [result.data], invalid: [] };
  }
  return { valid: [], invalid: [{ raw, error: result.error }] };
}

// ---------- USERS LOADER ----------
// Users is an array — parse each record individually so errors don't abort.

export async function loadUsers(filePath: string): Promise<LoadResult<User>> {
  const raw = await readJson(filePath);

  if (!Array.isArray(raw)) {
    const dummyError = new z.ZodError([
      {
        code: z.ZodIssueCode.custom,
        path: [],
        message: "Expected an array of users",
      },
    ]);
    return { valid: [], invalid: [{ raw, error: dummyError }] };
  }

  const valid: User[] = [];
  const invalid: { raw: unknown; error: z.ZodError }[] = [];

  for (const item of raw) {
    const result = UserSchema.safeParse(item);
    if (result.success) {
      valid.push(result.data);
    } else {
      invalid.push({ raw: item, error: result.error });
    }
  }

  return { valid, invalid };
}

// ---------- API RESPONSE LOADER ----------
// Single response object with a discriminated union at the top level.

export async function loadApiResponse(filePath: string): Promise<LoadResult<ApiResponse>> {
  const raw = await readJson(filePath);
  const result = ApiResponseSchema.safeParse(raw);

  if (result.success) {
    return { valid: [result.data], invalid: [] };
  }
  return { valid: [], invalid: [{ raw, error: result.error }] };
}
