/**
 * generate.ts — Generate a large NDJSON file for the ETL pipeline.
 *
 * Writes 100,000 EventRecord rows (configurable via ROW_COUNT env var) to
 * data/events.ndjson. Uses a seeded linear congruential generator so output
 * is deterministic and reproducible without any external dependencies.
 *
 * Usage:
 *   npx tsx data/generate.ts
 *   ROW_COUNT=1000000 npx tsx data/generate.ts
 */

import { createWriteStream } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";
import type { EventRecord } from "../src/schema.js";
import { CATEGORIES } from "../src/schema.js";

const __dirname = fileURLToPath(new URL(".", import.meta.url));
const OUTPUT_PATH = resolve(__dirname, "events.ndjson");
const ROW_COUNT = parseInt(process.env["ROW_COUNT"] ?? "100000", 10);

// ---------------------------------------------------------------------------
// Seeded PRNG — Linear Congruential Generator
// No external dependency. Deterministic for a given seed.
// ---------------------------------------------------------------------------

class LCG {
  private state: number;

  constructor(seed: number) {
    this.state = seed >>> 0; // ensure 32-bit unsigned
  }

  /** Return a float in [0, 1). */
  next(): number {
    // LCG parameters from Numerical Recipes
    this.state = (Math.imul(1664525, this.state) + 1013904223) >>> 0;
    return this.state / 0x1_0000_0000;
  }

  /** Return an integer in [min, max]. */
  int(min: number, max: number): number {
    return Math.floor(this.next() * (max - min + 1)) + min;
  }

  /** Pick a random element from an array. */
  pick<T>(arr: readonly T[]): T {
    const item = arr[this.int(0, arr.length - 1)];
    if (item === undefined) throw new Error("Empty array");
    return item;
  }

  /** Return a boolean with the given probability of being true. */
  bool(probability = 0.5): boolean {
    return this.next() < probability;
  }
}

// ---------------------------------------------------------------------------
// UUID-like string generator (not RFC-compliant, just looks like one)
// ---------------------------------------------------------------------------

function fakeUuid(rng: LCG): string {
  const hex = () => rng.int(0, 255).toString(16).padStart(2, "0");
  return [
    hex() + hex() + hex() + hex(),
    hex() + hex(),
    "4" + hex().slice(1) + hex(),
    ((rng.int(8, 11) * 16) | rng.int(0, 15)).toString(16) + hex(),
    hex() + hex() + hex() + hex() + hex() + hex(),
  ].join("-");
}

// ---------------------------------------------------------------------------
// Async generator that produces EventRecord rows
// ---------------------------------------------------------------------------

async function* generateEvents(count: number): AsyncGenerator<EventRecord> {
  const rng = new LCG(0xdeadbeef); // fixed seed for reproducibility
  const baseTs = 1_700_000_000; // Nov 2023

  for (let i = 1; i <= count; i++) {
    const record: EventRecord = {
      id: i,
      ts: baseTs + rng.int(0, 86_400 * 365), // random second within 1 year
      category: rng.pick(CATEGORIES),
      userId: fakeUuid(rng),
      amountCents: rng.int(99, 99_999), // $0.99 – $999.99
      quantity: rng.int(1, 20),
      flagged: rng.bool(0.02), // ~2% flagged
    };
    yield record;
  }
}

// ---------------------------------------------------------------------------
// Transform generator output to NDJSON lines
// ---------------------------------------------------------------------------

async function* toNdjsonLines(
  events: AsyncGenerator<EventRecord>
): AsyncGenerator<string> {
  for await (const event of events) {
    yield JSON.stringify(event) + "\n";
  }
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

console.log(`Generating ${ROW_COUNT.toLocaleString()} events → ${OUTPUT_PATH}`);
const start = Date.now();

await pipeline(
  Readable.from(toNdjsonLines(generateEvents(ROW_COUNT))),
  createWriteStream(OUTPUT_PATH)
);

const elapsed = Date.now() - start;
console.log(`Done. Wrote ${ROW_COUNT.toLocaleString()} rows in ${elapsed} ms.`);
