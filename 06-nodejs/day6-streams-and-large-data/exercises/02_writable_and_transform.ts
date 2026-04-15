/**
 * Exercise 02 — Writable Streams & Transform Streams
 *
 * Topics: fs.createWriteStream, custom Transform class, pipeline from
 *         node:stream/promises, reading back to verify output.
 *
 * Run: npx tsx 06-nodejs/day6-streams-and-large-data/exercises/02_writable_and_transform.ts
 */

import { createReadStream, createWriteStream, writeFileSync, readFileSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Transform, type TransformCallback } from "node:stream";
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";
import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Custom Transforms
// ---------------------------------------------------------------------------

/**
 * UpperCaseTransform — receives Buffer/string chunks, emits uppercased string chunks.
 * Converts Buffer to string explicitly so it works regardless of the upstream
 * source (file stream, Readable.from, etc.).
 */
class UpperCaseTransform extends Transform {
  constructor() {
    super({ encoding: "utf8" });
  }

  override _transform(
    chunk: Buffer | string,
    _encoding: BufferEncoding,
    callback: TransformCallback
  ): void {
    throw new Error("TODO: implement UpperCaseTransform._transform");
  }
}

/**
 * PrefixTransform — prepends a fixed string to every line in the stream.
 * Handles the case where a chunk may contain multiple lines.
 */
class PrefixTransform extends Transform {
  private readonly prefix: string;
  private leftover: string = "";

  constructor(prefix: string) {
    super({ encoding: "utf8" });
    this.prefix = prefix;
  }

  override _transform(
    chunk: Buffer | string,
    _encoding: BufferEncoding,
    callback: TransformCallback
  ): void {
    throw new Error("TODO: implement PrefixTransform._transform");
  }

  override _flush(callback: TransformCallback): void {
    throw new Error("TODO: implement PrefixTransform._flush");
  }
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
  const tmpIn = join(tmpdir(), `day6_ex02_in_${process.pid}.txt`);
  const tmpOut = join(tmpdir(), `day6_ex02_out_${process.pid}.txt`);

  try {
    // -----------------------------------------------------------------------
    // Test 1: pipeline with UpperCaseTransform
    // -----------------------------------------------------------------------
    const original = "hello world\nfoo bar\nbaz qux";
    writeFileSync(tmpIn, original, "utf8");

    await pipeline(
      createReadStream(tmpIn, { encoding: "utf8" }),
      new UpperCaseTransform(),
      createWriteStream(tmpOut)
    );

    const result1 = readFileSync(tmpOut, "utf8");
    assert.equal(result1, original.toUpperCase(), "UpperCaseTransform produced wrong output");

    // -----------------------------------------------------------------------
    // Test 2: pipeline with PrefixTransform
    // -----------------------------------------------------------------------
    const lines = "alpha\nbeta\ngamma";
    writeFileSync(tmpIn, lines, "utf8");

    await pipeline(
      createReadStream(tmpIn, { encoding: "utf8" }),
      new PrefixTransform(">> "),
      createWriteStream(tmpOut)
    );

    const result2 = readFileSync(tmpOut, "utf8");
    const expectedPrefixed = ">> alpha\n>> beta\n>> gamma";
    assert.equal(result2, expectedPrefixed, "PrefixTransform produced wrong output");

    // -----------------------------------------------------------------------
    // Test 3: chained transforms (uppercase then prefix)
    // -----------------------------------------------------------------------
    const input3 = "hello\nworld";
    writeFileSync(tmpIn, input3, "utf8");

    await pipeline(
      createReadStream(tmpIn, { encoding: "utf8" }),
      new UpperCaseTransform(),
      new PrefixTransform("- "),
      createWriteStream(tmpOut)
    );

    const result3 = readFileSync(tmpOut, "utf8");
    const expected3 = "- HELLO\n- WORLD";
    assert.equal(result3, expected3, "Chained transforms produced wrong output");

    // -----------------------------------------------------------------------
    // Test 4: Readable.from + transform + writable (no input file needed)
    // -----------------------------------------------------------------------
    const sourceData = ["chunk one", " chunk two", " chunk three"];

    await pipeline(
      Readable.from(sourceData, { objectMode: false }),
      new UpperCaseTransform(),
      createWriteStream(tmpOut)
    );

    const result4 = readFileSync(tmpOut, "utf8");
    assert.equal(
      result4,
      sourceData.join("").toUpperCase(),
      "Readable.from + transform produced wrong output"
    );

    // -----------------------------------------------------------------------
    // Test 5: writing an empty stream produces an empty file
    // -----------------------------------------------------------------------
    await pipeline(
      Readable.from([], { objectMode: false }),
      new UpperCaseTransform(),
      createWriteStream(tmpOut)
    );

    const result5 = readFileSync(tmpOut, "utf8");
    assert.equal(result5, "", "Empty pipeline should produce empty output");
  } finally {
    for (const f of [tmpIn, tmpOut]) {
      try { unlinkSync(f); } catch { /* already gone */ }
    }
  }

  console.log("All tests passed!");
}

await main();
