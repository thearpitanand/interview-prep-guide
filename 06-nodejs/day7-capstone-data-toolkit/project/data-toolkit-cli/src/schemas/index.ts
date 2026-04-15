// schemas/index.ts — Named Zod schemas for the `validate` command.

import { z } from "zod";

// ---- Schema definitions ----

// TODO: define UserSchema
export const UserSchema = z.unknown();

// TODO: define TransactionSchema
export const TransactionSchema = z.unknown();

// TODO: define OrderSchema
export const OrderSchema = z.unknown();

// ---- Registry ----

export type SchemaName = "user" | "transaction" | "order";

export const schemaRegistry = {
  user: UserSchema,
  transaction: TransactionSchema,
  order: OrderSchema,
} as const satisfies Record<SchemaName, z.ZodTypeAny>;

export function getSchema(name: string): z.ZodTypeAny | undefined {
  throw new Error("TODO: implement getSchema");
}

export const availableSchemas = Object.keys(schemaRegistry) as SchemaName[];
