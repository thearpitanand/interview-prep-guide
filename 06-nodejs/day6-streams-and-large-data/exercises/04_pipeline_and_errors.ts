/**
 * Exercise 04 — pipeline and Error Propagation
 *
 * Topics: pipeline from node:stream/promises, error propagation through
 *         a multi-stage pipeline, stream cleanup on failure, poison-pill
 *         inputs, try/catch around awaited pipeline.
 *
 * Run: npx tsx 06-nodejs/day6-streams-and-large-data/exercises/04_pipeline_and_errors.ts
 */

import {
  createReadStream,
  createWriteStream,
  writeFileSync,
  readFileSync,
  unlinkSync,
  existsSync,
} from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { Transform, type TransformCallback, Readable } from "node:stream";
import { pipeline } from "node:stream/promises";
import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Transforms
// ---------------------------------------------------------------------------

const POISON = "__ERROR__";

/**
 * A Transform that passes chunks through unchanged UNLESS the chunk (trimmed)
 * equals the poison string, in which case it emits an error.
 *
 * NOTE: This works correctly when the upstream emits one discrete item per
 * write (e.g., Readable.from an array). For file streams that may coalesce
 * multiple lines into one chunk, use a line-splitting transform first.
 */
class PoisonRejectTransform extends Transform {
  constructor() {
    super({ encoding: "utf8" });
  }

  override _transform(
    chunk: Buffer | string,
    _encoding: BufferEncoding,
    callback: TransformCallback
  ): void {
    throw new Error("TODO: implement PoisonRejectTransform._transform");
  }
}

/**
 * A Transform that converts each chunk to uppercase.
 */
class UpperTransform extends Transform {
  constructor() {
    super({ encoding: "utf8" });
  }

  override _transform(
    chunk: Buffer | string,
    _encoding: BufferEncoding,
    callback: TransformCallback
  ): void {
    throw new Error("TODO: implement UpperTransform._transform");
  }
}

/**
 * A Transform that errors if any chunk contains a specific substring.
 * Useful for testing error propagation with file stream sources (which may
 * deliver multi-line chunks).
 */
class ContainsPoisonTransform extends Transform {
  private readonly poison: string;

  constructor(poison: string) {
    super({ encoding: "utf8" });
    this.poison = poison;
  }

  override _transform(
    chunk: Buffer | string,
    _encoding: BufferEncoding,
    callback: TransformCallback
  ): void {
    throw new Error("TODO: implement ContainsPoisonTransform._transform");
  }
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
  const tmpIn = join(tmpdir(), `day6_ex04_in_${process.pid}.txt`);
  const tmpOut = join(tmpdir(), `day6_ex04_out_${process.pid}.txt`);

  try {
    // -----------------------------------------------------------------------
    // Test 1: happy-path pipeline succeeds
    // -----------------------------------------------------------------------
    const happyInput = "hello world\nfoo bar";
    writeFileSync(tmpIn, happyInput, "utf8");

    await pipeline(
      createReadStream(tmpIn, { encoding: "utf8" }),
      new UpperTransform(),
      createWriteStream(tmpOut)
    );

    const happyResult = readFileSync(tmpOut, "utf8");
    assert.equal(
      happyResult,
      happyInput.toUpperCase(),
      "Happy-path pipeline should uppercase content"
    );

    // -----------------------------------------------------------------------
    // Test 2: pipeline rejects when a transform errors (Readable.from source)
    // Readable.from(array) emits one item per array element, so each chunk is
    // exactly one string — trim() === POISON works correctly here.
    // -----------------------------------------------------------------------
    let caughtError: Error | null = null;

    try {
      await pipeline(
        Readable.from(["good line", POISON, "another line"]),
        new PoisonRejectTransform(),
        createWriteStream(tmpOut)
      );
    } catch (err) {
      caughtError = err as Error;
    }

    assert.ok(caughtError !== null, "pipeline should have thrown on poison item");
    assert.ok(
      caughtError.message.includes("Poison"),
      `Error message should mention 'Poison', got: "${caughtError.message}"`
    );

    // -----------------------------------------------------------------------
    // Test 3: error in a middle transform propagates (UpperTransform → PoisonRejectTransform)
    // UpperTransform passes each item through unchanged (POISON is all-caps already).
    // PoisonRejectTransform then receives each item individually and errors.
    // -----------------------------------------------------------------------
    caughtError = null;

    try {
      await pipeline(
        Readable.from(["good", POISON, "also good"]),
        new UpperTransform(),       // POISON stays "__ERROR__" after upper
        new PoisonRejectTransform(), // errors on "__ERROR__"
        createWriteStream(tmpOut)
      );
    } catch (err) {
      caughtError = err as Error;
    }

    assert.ok(
      caughtError !== null,
      "Error in middle transform should reject the whole pipeline"
    );

    // -----------------------------------------------------------------------
    // Test 4: error propagates from file-stream source using ContainsPoison
    // -----------------------------------------------------------------------
    const FILE_POISON = "BADTOKEN";
    writeFileSync(tmpIn, `first line\nsecond line with ${FILE_POISON} in it\nthird line`, "utf8");

    caughtError = null;

    try {
      await pipeline(
        createReadStream(tmpIn, { encoding: "utf8" }),
        new ContainsPoisonTransform(FILE_POISON),
        createWriteStream(tmpOut)
      );
    } catch (err) {
      caughtError = err as Error;
    }

    assert.ok(
      caughtError !== null,
      "ContainsPoisonTransform should reject the pipeline on poison content"
    );
    assert.ok(
      caughtError.message.includes(FILE_POISON),
      `Error message should contain the poison token, got: "${caughtError.message}"`
    );

    // -----------------------------------------------------------------------
    // Test 5: after a failed pipeline, re-running with clean input succeeds
    // -----------------------------------------------------------------------
    const cleanInput = "line one\nline two\nline three";
    writeFileSync(tmpIn, cleanInput, "utf8");

    await pipeline(
      createReadStream(tmpIn, { encoding: "utf8" }),
      new UpperTransform(),
      createWriteStream(tmpOut)
    );

    const cleanResult = readFileSync(tmpOut, "utf8");
    assert.equal(
      cleanResult,
      cleanInput.toUpperCase(),
      "Pipeline after error recovery should work correctly"
    );

    // -----------------------------------------------------------------------
    // Test 6: output file exists after partial write (pipeline failed midway)
    // -----------------------------------------------------------------------
    const FILE_POISON2 = "STOP_HERE";
    // Data where poison appears partway through
    writeFileSync(
      tmpIn,
      `good data first\n${FILE_POISON2} triggers error\nmore data`,
      "utf8"
    );

    caughtError = null;
    try {
      await pipeline(
        createReadStream(tmpIn, { encoding: "utf8" }),
        new ContainsPoisonTransform(FILE_POISON2),
        createWriteStream(tmpOut)
      );
    } catch (err) {
      caughtError = err as Error;
    }

    assert.ok(caughtError !== null, "Partial pipeline should have errored");
    assert.ok(existsSync(tmpOut), "Output file should exist even after partial write");
  } finally {
    for (const f of [tmpIn, tmpOut]) {
      try { unlinkSync(f); } catch { /* already gone */ }
    }
  }

  console.log("All tests passed!");
}

await main();
