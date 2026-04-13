// schemas/index.ts — Named Zod schemas for the `validate` command.

import { z } from "zod";

// ---- Schema definitions ----

export const UserSchema = z.object({
  id: z.number({ coerce: true }).int().positive(),
  name: z.string().min(1),
  age: z.number({ coerce: true }).int().min(0).max(150),
  role: z.enum(["admin", "user", "moderator"]),
  address: z
    .object({
      city: z.string().min(1),
      country: z.string().length(2),
    })
    .optional(),
});

export const TransactionSchema = z.object({
  txId: z.string().min(1),
  userId: z.number({ coerce: true }).int().positive(),
  type: z.enum(["debit", "credit"]),
  amount: z.number({ coerce: true }).positive(),
  currency: z.string().length(3),
  timestamp: z.string().datetime({ offset: true }),
});

export const OrderSchema = z.object({
  orderId: z.string().min(1),
  userId: z.number({ coerce: true }).int().positive(),
  product: z.string().min(1),
  category: z.string().min(1),
  quantity: z.number({ coerce: true }).int().positive(),
  amount: z.number({ coerce: true }).positive(),
  status: z.enum(["pending", "shipped", "delivered", "cancelled"]),
});

// ---- Registry ----

export type SchemaName = "user" | "transaction" | "order";

export const schemaRegistry = {
  user: UserSchema,
  transaction: TransactionSchema,
  order: OrderSchema,
} as const satisfies Record<SchemaName, z.ZodTypeAny>;

export function getSchema(name: string): z.ZodTypeAny | undefined {
  if (name in schemaRegistry) {
    return schemaRegistry[name as SchemaName];
  }
  return undefined;
}

export const availableSchemas = Object.keys(schemaRegistry) as SchemaName[];
