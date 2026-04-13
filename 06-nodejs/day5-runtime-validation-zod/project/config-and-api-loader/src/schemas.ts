/**
 * schemas.ts — All Zod schemas for the config-and-api-loader project.
 *
 * Schemas are the single source of truth. TypeScript types are derived
 * via z.infer — no separate interfaces or type aliases elsewhere.
 */
import { z } from "zod";

// ---------- CONFIG SCHEMA ----------

const DatabaseConfigSchema = z.object({
  host: z.string().min(1),
  port: z.number().int().min(1).max(65535),
  name: z.string().min(1),
  poolSize: z.number().int().min(1).max(100),
  sslMode: z.enum(["disable", "require", "verify-ca", "verify-full"]),
  migrationDir: z.string(),
});

const ServerConfigSchema = z.object({
  host: z.string(),
  port: z.number().int().min(1).max(65535),
  tlsEnabled: z.boolean(),
  maxConnections: z.number().int().positive(),
});

const RedisConfigSchema = z.object({
  host: z.string(),
  port: z.number().int().min(1).max(65535),
  db: z.number().int().min(0),
  ttlSeconds: z.number().int().positive(),
});

const LoggingConfigSchema = z.object({
  level: z.enum(["debug", "info", "warn", "error"]),
  format: z.enum(["json", "text"]),
  destinations: z.array(z.enum(["stdout", "stderr", "file"])),
  filePath: z.string().optional(),
});

const FeaturesConfigSchema = z.object({
  enableNewDashboard: z.boolean(),
  enableBetaExport: z.boolean(),
  maxUploadMb: z.number().int().positive(),
  allowedOrigins: z.array(z.string().url()),
});

const AppMetaSchema = z.object({
  name: z.string().min(1),
  version: z.string().regex(/^\d+\.\d+\.\d+$/, "Version must be semver"),
  environment: z.enum(["development", "staging", "production", "test"]),
});

export const ConfigSchema = z.object({
  app: AppMetaSchema,
  server: ServerConfigSchema,
  database: DatabaseConfigSchema,
  redis: RedisConfigSchema.optional(),
  logging: LoggingConfigSchema,
  features: FeaturesConfigSchema,
});

export type Config = z.infer<typeof ConfigSchema>;

// ---------- USER SCHEMA ----------

const AddressSchema = z.object({
  street: z.string().min(1),
  city: z.string().min(1),
  state: z.string().length(2),
  zip: z.string().regex(/^\d{5}$/, "ZIP must be exactly 5 digits"),
});

export const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string().min(1),
  age: z.number().int().min(0).max(150),
  role: z.enum(["admin", "user", "moderator"]),
  address: AddressSchema,
  bio: z.string().max(500).optional(),
});

export type User = z.infer<typeof UserSchema>;
export type Address = z.infer<typeof AddressSchema>;

// ---------- API RESPONSE SCHEMA ----------

const ApiResultSchema = z.object({
  id: z.string(),
  type: z.enum(["transaction", "event", "refund"]),
  amount: z.number().nonnegative(),
  currency: z.string().length(3),
  description: z.string(),
  occurredAt: z.coerce.date(),
});

const ApiMetaSchema = z.object({
  page: z.number().int().positive(),
  pageSize: z.number().int().positive(),
  total: z.number().int().nonnegative(),
});

// Discriminated union: success vs error response
export const ApiResponseSchema = z.discriminatedUnion("status", [
  z.object({
    status: z.literal("success"),
    requestId: z.string(),
    timestamp: z.coerce.date(),
    meta: ApiMetaSchema,
    results: z.array(ApiResultSchema),
  }),
  z.object({
    status: z.literal("error"),
    requestId: z.string(),
    timestamp: z.coerce.date(),
    code: z.string(),
    message: z.string(),
  }),
]);

export type ApiResponse = z.infer<typeof ApiResponseSchema>;
export type ApiResult = z.infer<typeof ApiResultSchema>;
