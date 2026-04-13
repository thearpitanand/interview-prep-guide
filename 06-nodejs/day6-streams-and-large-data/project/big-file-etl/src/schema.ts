/**
 * schema.ts — Zod schema for the event records processed by the ETL pipeline.
 *
 * Each line of events.ndjson represents one EventRecord.
 */

import { z } from "zod";

export const CATEGORIES = [
  "electronics",
  "books",
  "clothing",
  "food",
  "sports",
  "home",
  "toys",
  "beauty",
  "automotive",
  "garden",
  "office",
  "health",
  "music",
  "travel",
  "finance",
  "gaming",
  "education",
  "media",
  "pets",
  "other",
] as const;

export type Category = (typeof CATEGORIES)[number];

export const EventRecordSchema = z.object({
  /** Unique event identifier. */
  id: z.number().int().positive(),

  /** Unix timestamp in seconds. */
  ts: z.number().int().nonnegative(),

  /** Event category — one of the 20 known values. Bounded key cardinality. */
  category: z.enum(CATEGORIES),

  /** User identifier — UUID v4 string. */
  userId: z.string().min(1),

  /** Monetary amount for this event, in cents. */
  amountCents: z.number().int().nonnegative(),

  /** Number of items involved. */
  quantity: z.number().int().positive(),

  /** Whether the event was flagged as fraudulent. */
  flagged: z.boolean(),
});

export type EventRecord = z.infer<typeof EventRecordSchema>;

/** Aggregated summary per category, written to the output CSV. */
export interface CategorySummary {
  category: Category;
  event_count: number;
  total_amount_cents: number;
  total_quantity: number;
  flagged_count: number;
  avg_amount_cents: number;
}
