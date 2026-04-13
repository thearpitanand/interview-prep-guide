/**
 * Exercise 01 — Readable Streams
 *
 * Topics: fs.createReadStream, for await...of on a Readable,
 *         encoding option, byte-count assertion.
 *
 * Run: npx tsx 06-nodejs/day6-streams-and-large-data/exercises/01_readable_streams.ts
 */

import { createReadStream, writeFileSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/**
 * Read an entire stream via async iteration and return the total byte length
 * of all chunks received. Chunks arrive as strings (encoding is set on the
 * stream), so we measure UTF-8 byte length with Buffer.byteLength.
 */
async function totalByteLength(filePath: string): Promise<number> {
  const stream = createReadStream(filePath, { encoding: "utf8" });
  let total = 0;

  for await (const chunk of stream) {
    // chunk is a string because we set encoding: "utf8"
    total += Buffer.byteLength(chunk as string, "utf8");
  }

  return total;
}

/**
 * Read a stream and collect all chunks into a single string.
 * This is fine for small test data — not for production large files!
 */
async function readAll(filePath: string): Promise<string> {
  const stream = createReadStream(filePath, { encoding: "utf8" });
  const parts: string[] = [];

  for await (const chunk of stream) {
    parts.push(chunk as string);
  }

  return parts.join("");
}

/**
 * Read a stream with a small highWaterMark to verify that multiple chunks
 * are produced and the data is reassembled correctly.
 */
async function readWithSmallBuffer(
  filePath: string,
  hwm: number
): Promise<{ chunks: number; content: string }> {
  const stream = createReadStream(filePath, {
    encoding: "utf8",
    highWaterMark: hwm,
  });
  const parts: string[] = [];
  let chunkCount = 0;

  for await (const chunk of stream) {
    parts.push(chunk as string);
    chunkCount++;
  }

  return { chunks: chunkCount, content: parts.join("") };
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
  const tmpFile = join(tmpdir(), `day6_ex01_${process.pid}.txt`);

  try {
    // -----------------------------------------------------------------------
    // Test 1: basic byte count
    // -----------------------------------------------------------------------
    const content = "Hello, streams!\nLine two.\nLine three.";
    writeFileSync(tmpFile, content, "utf8");

    const expected = Buffer.byteLength(content, "utf8");
    const actual = await totalByteLength(tmpFile);

    assert.equal(actual, expected, `Byte count mismatch: got ${actual}, want ${expected}`);

    // -----------------------------------------------------------------------
    // Test 2: content reconstruction
    // -----------------------------------------------------------------------
    const reconstructed = await readAll(tmpFile);
    assert.equal(reconstructed, content, "Reconstructed content does not match original");

    // -----------------------------------------------------------------------
    // Test 3: small highWaterMark forces multiple chunks
    // -----------------------------------------------------------------------
    // Each chunk is at most 8 bytes, so a 37-byte file must produce > 1 chunk.
    const { chunks, content: rebuilt } = await readWithSmallBuffer(tmpFile, 8);

    assert.ok(chunks > 1, `Expected multiple chunks with hwm=8, got ${chunks}`);
    assert.equal(rebuilt, content, "Content after small-buffer read does not match");

    // -----------------------------------------------------------------------
    // Test 4: multi-byte UTF-8 characters are not corrupted
    // -----------------------------------------------------------------------
    const emoji = "Hello 🌊 stream 🚀";
    writeFileSync(tmpFile, emoji, "utf8");

    // Use hwm=4 to ensure chunks split across multi-byte chars
    const { content: emojiRebuilt } = await readWithSmallBuffer(tmpFile, 4);
    assert.equal(
      emojiRebuilt,
      emoji,
      "Multi-byte characters were corrupted across chunk boundaries"
    );

    // -----------------------------------------------------------------------
    // Test 5: empty file produces zero bytes and zero chunks
    // -----------------------------------------------------------------------
    writeFileSync(tmpFile, "", "utf8");
    const emptyBytes = await totalByteLength(tmpFile);
    assert.equal(emptyBytes, 0, "Empty file should yield 0 bytes");

    const emptyContent = await readAll(tmpFile);
    assert.equal(emptyContent, "", "Empty file should yield empty string");
  } finally {
    unlinkSync(tmpFile);
  }

  console.log("All tests passed!");
}

await main();
