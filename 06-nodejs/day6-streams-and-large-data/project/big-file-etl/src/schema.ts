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

// TODO: define EventRecordSchema
export const EventRecordSchema = z.unknown();

export type EventRecord = z.infer<typeof EventRecordSchema>;

/** Aggregated summary per category, written to the output CSV. */
export interface CategorySummary {
  /* TODO */
}
