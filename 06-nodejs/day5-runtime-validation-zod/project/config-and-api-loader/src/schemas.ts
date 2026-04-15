/**
 * schemas.ts — All Zod schemas for the config-and-api-loader project.
 *
 * Schemas are the single source of truth. TypeScript types are derived
 * via z.infer — no separate interfaces or type aliases elsewhere.
 */
import { z } from "zod";

// ---------- CONFIG SCHEMA ----------

// TODO: define ConfigSchema
export const ConfigSchema = z.unknown();

export type Config = z.infer<typeof ConfigSchema>;

// ---------- USER SCHEMA ----------

// TODO: define UserSchema
export const UserSchema = z.unknown();

export type User = z.infer<typeof UserSchema>;
export type Address = unknown; // TODO: define Address

// ---------- API RESPONSE SCHEMA ----------

// TODO: define ApiResponseSchema
export const ApiResponseSchema = z.unknown();

export type ApiResponse = z.infer<typeof ApiResponseSchema>;
export type ApiResult = unknown; // TODO: define ApiResult
