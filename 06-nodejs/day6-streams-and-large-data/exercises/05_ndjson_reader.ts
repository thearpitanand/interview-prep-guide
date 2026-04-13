/**
 * Exercise 05 — NDJSON Streaming Reader
 *
 * Topics: readline.createInterface as async iterable, async generator for
 *         line-by-line parsing, malformed-line handling, typed generic helper.
 *
 * Run: npx tsx 06-nodejs/day6-streams-and-large-data/exercises/05_ndjson_reader.ts
 */

import { createReadStream, writeFileSync, unlinkSync } from "node:fs";
import { createInterface } from "node:readline";
import { tmpdir } from "node:os";
import { join } from "node:path";
import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// readNdjson helper
// ---------------------------------------------------------------------------

interface NdjsonReadResult<T> {
  records: AsyncGenerator<T>;
  /** Resolves after the generator is fully consumed with the count of skipped lines. */
  skippedLines: () => number;
}

/**
 * Stream-parse an NDJSON file, yielding one typed record per line.
 *
 * - Skips blank lines silently.
 * - Skips malformed lines (bad JSON) without throwing; calls onMalformed if provided.
 * - Never holds more than one line in memory at a time.
 *
 * @param path     Absolute path to the NDJSON file.
 * @param onMalformed  Optional callback for bad lines (line text + parse error).
 */
async function* readNdjson<T>(
  path: string,
  onMalformed?: (line: string, err: unknown) => void
): AsyncGenerator<T> {
  const fileStream = createReadStream(path, { encoding: "utf8" });
  const rl = createInterface({
    input: fileStream,
    crlfDelay: Infinity,
  });

  for await (const line of rl) {
    const trimmed = line.trim();
    if (!trimmed) continue; // skip blank lines
    try {
      yield JSON.parse(trimmed) as T;
    } catch (err) {
      onMalformed?.(trimmed, err);
    }
  }
}

// ---------------------------------------------------------------------------
// Helper — collect async iterable to array
// ---------------------------------------------------------------------------

async function toArray<T>(iter: AsyncIterable<T>): Promise<T[]> {
  const results: T[] = [];
  for await (const item of iter) results.push(item);
  return results;
}

// ---------------------------------------------------------------------------
// Test types
// ---------------------------------------------------------------------------

interface Event {
  id: number;
  type: string;
  value: number;
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
  const tmpFile = join(tmpdir(), `day6_ex05_${process.pid}.ndjson`);

  try {
    // -----------------------------------------------------------------------
    // Test 1: read 5 well-formed objects
    // -----------------------------------------------------------------------
    const events: Event[] = [
      { id: 1, type: "click", value: 10 },
      { id: 2, type: "view", value: 5 },
      { id: 3, type: "click", value: 20 },
      { id: 4, type: "scroll", value: 1 },
      { id: 5, type: "view", value: 8 },
    ];

    writeFileSync(tmpFile, events.map((e) => JSON.stringify(e)).join("\n"), "utf8");

    const readEvents = await toArray(readNdjson<Event>(tmpFile));

    assert.equal(readEvents.length, 5, `Expected 5 records, got ${readEvents.length}`);
    assert.deepEqual(readEvents, events, "Parsed records do not match original events");

    // -----------------------------------------------------------------------
    // Test 2: values are correctly typed after parsing
    // -----------------------------------------------------------------------
    const first = readEvents[0];
    assert.ok(first !== undefined, "First event should exist");
    assert.equal(typeof first.id, "number", "id should be a number");
    assert.equal(typeof first.type, "string", "type should be a string");
    assert.equal(typeof first.value, "number", "value should be a number");

    // -----------------------------------------------------------------------
    // Test 3: malformed lines are skipped and reported
    // -----------------------------------------------------------------------
    const mixedContent = [
      JSON.stringify({ id: 1, type: "click", value: 1 }),
      "not valid json {{{{",                           // malformed
      JSON.stringify({ id: 2, type: "view", value: 2 }),
      "",                                              // blank line
      "{ broken",                                      // malformed
      JSON.stringify({ id: 3, type: "scroll", value: 3 }),
      "   ",                                           // whitespace-only
    ].join("\n");

    writeFileSync(tmpFile, mixedContent, "utf8");

    const malformedLines: string[] = [];
    const goodRecords = await toArray(
      readNdjson<Event>(tmpFile, (line) => malformedLines.push(line))
    );

    assert.equal(goodRecords.length, 3, `Expected 3 good records, got ${goodRecords.length}`);
    assert.equal(malformedLines.length, 2, `Expected 2 malformed lines, got ${malformedLines.length}`);
    assert.ok(malformedLines[0]?.includes("not valid json"), "First malformed line mismatch");
    assert.ok(malformedLines[1]?.includes("broken"), "Second malformed line mismatch");

    // -----------------------------------------------------------------------
    // Test 4: blank lines and whitespace-only lines are silently skipped
    // -----------------------------------------------------------------------
    const sparseContent = [
      "",
      "   ",
      JSON.stringify({ id: 1, type: "a", value: 0 }),
      "",
      JSON.stringify({ id: 2, type: "b", value: 0 }),
      "\t",
    ].join("\n");

    writeFileSync(tmpFile, sparseContent, "utf8");

    const sparseResult = await toArray(readNdjson<Event>(tmpFile));
    assert.equal(sparseResult.length, 2, "Only 2 valid records in sparse content");

    // -----------------------------------------------------------------------
    // Test 5: empty file yields no records
    // -----------------------------------------------------------------------
    writeFileSync(tmpFile, "", "utf8");
    const emptyResult = await toArray(readNdjson<Event>(tmpFile));
    assert.equal(emptyResult.length, 0, "Empty file should yield 0 records");

    // -----------------------------------------------------------------------
    // Test 6: single-object file (no trailing newline)
    // -----------------------------------------------------------------------
    const single: Event = { id: 99, type: "test", value: 42 };
    writeFileSync(tmpFile, JSON.stringify(single), "utf8"); // no \n at end

    const singleResult = await toArray(readNdjson<Event>(tmpFile));
    assert.equal(singleResult.length, 1, "Single-line file should yield 1 record");
    assert.deepEqual(singleResult[0], single, "Single record should match");

    // -----------------------------------------------------------------------
    // Test 7: partial consumption via for await + break
    // -----------------------------------------------------------------------
    const manyEvents = Array.from({ length: 100 }, (_, i) => ({
      id: i + 1,
      type: "event",
      value: i,
    }));
    writeFileSync(
      tmpFile,
      manyEvents.map((e) => JSON.stringify(e)).join("\n"),
      "utf8"
    );

    let consumed = 0;
    for await (const _ of readNdjson<Event>(tmpFile)) {
      consumed++;
      if (consumed === 10) break;
    }

    assert.equal(consumed, 10, "Breaking out of loop should stop after 10 records");
  } finally {
    try { unlinkSync(tmpFile); } catch { /* already gone */ }
  }

  console.log("All tests passed!");
}

await main();
