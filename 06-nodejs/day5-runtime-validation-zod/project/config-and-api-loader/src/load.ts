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

// ---------- CONFIG LOADER ----------
// Config is a single object, not an array — either it parses or it doesn't.

export async function loadConfig(filePath: string): Promise<LoadResult<Config>> {
  throw new Error("TODO: implement loadConfig");
}

// ---------- USERS LOADER ----------
// Users is an array — parse each record individually so errors don't abort.

export async function loadUsers(filePath: string): Promise<LoadResult<User>> {
  throw new Error("TODO: implement loadUsers");
}

// ---------- API RESPONSE LOADER ----------
// Single response object with a discriminated union at the top level.

export async function loadApiResponse(filePath: string): Promise<LoadResult<ApiResponse>> {
  throw new Error("TODO: implement loadApiResponse");
}
