/**
 * Exercise 03 — Async Iterators & Generators
 *
 * Topics: async function*, yield, for await...of, custom async iterator
 *         utilities (take, map, filter, batch), composing generators.
 *
 * Run: npx tsx 06-nodejs/day6-streams-and-large-data/exercises/03_async_iterators.ts
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Core async generators
// ---------------------------------------------------------------------------

/**
 * Yield integers from start to end (inclusive) with a tiny async delay to
 * simulate real async work (e.g., reading from a socket or database cursor).
 */
async function* range(start: number, end: number): AsyncGenerator<number> {
  throw new Error("TODO: implement range");
  yield undefined as never; // unreachable — present only so TS recognizes the generator signature
}

/**
 * Yield items from a source array one-by-one with an optional delay.
 * Useful for turning static test data into an async iterable.
 */
async function* fromArray<T>(items: T[], delayMs = 0): AsyncGenerator<T> {
  throw new Error("TODO: implement fromArray");
  yield undefined as never; // unreachable — present only so TS recognizes the generator signature
}

// ---------------------------------------------------------------------------
// Higher-order async iterator utilities
// ---------------------------------------------------------------------------

/**
 * Take the first n items from an async iterable.
 * Breaking out of the loop destroys the underlying generator (calls .return()).
 */
async function* take<T>(iter: AsyncIterable<T>, n: number): AsyncGenerator<T> {
  throw new Error("TODO: implement take");
  yield undefined as never; // unreachable — present only so TS recognizes the generator signature
}

/**
 * Map each item through an async transform function.
 */
async function* map<T, U>(
  iter: AsyncIterable<T>,
  fn: (item: T) => U | Promise<U>
): AsyncGenerator<U> {
  throw new Error("TODO: implement map");
  yield undefined as never; // unreachable — present only so TS recognizes the generator signature
}

/**
 * Filter items using an async predicate.
 */
async function* filter<T>(
  iter: AsyncIterable<T>,
  pred: (item: T) => boolean | Promise<boolean>
): AsyncGenerator<T> {
  throw new Error("TODO: implement filter");
  yield undefined as never; // unreachable — present only so TS recognizes the generator signature
}

/**
 * Batch items into arrays of at most `size` elements.
 * The last batch may be smaller.
 */
async function* batch<T>(
  iter: AsyncIterable<T>,
  size: number
): AsyncGenerator<T[]> {
  throw new Error("TODO: implement batch");
  yield undefined as never; // unreachable — present only so TS recognizes the generator signature
}

/**
 * Collect an entire async iterable into an array.
 * Only safe for small/bounded iterables — defeats the streaming purpose otherwise.
 */
async function toArray<T>(iter: AsyncIterable<T>): Promise<T[]> {
  throw new Error("TODO: implement toArray");
}

/**
 * Count items in an async iterable without collecting them.
 */
async function count(iter: AsyncIterable<unknown>): Promise<number> {
  throw new Error("TODO: implement count");
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

async function main(): Promise<void> {
  // -----------------------------------------------------------------------
  // Test 1: range produces correct values
  // -----------------------------------------------------------------------
  const nums = await toArray(range(1, 5));
  assert.deepEqual(nums, [1, 2, 3, 4, 5], "range(1,5) should yield [1,2,3,4,5]");

  // -----------------------------------------------------------------------
  // Test 2: take limits the output
  // -----------------------------------------------------------------------
  const first3 = await toArray(take(range(1, 100), 3));
  assert.deepEqual(first3, [1, 2, 3], "take(range(1,100), 3) should yield [1,2,3]");

  // take(0) should yield nothing
  const takeZero = await toArray(take(range(1, 10), 0));
  assert.deepEqual(takeZero, [], "take(range, 0) should yield []");

  // -----------------------------------------------------------------------
  // Test 3: map transforms values
  // -----------------------------------------------------------------------
  const doubled = await toArray(map(range(1, 4), (n) => n * 2));
  assert.deepEqual(doubled, [2, 4, 6, 8], "map should double each value");

  // map with async fn
  const asyncMapped = await toArray(
    map(range(1, 3), async (n) => {
      await Promise.resolve();
      return n.toString();
    })
  );
  assert.deepEqual(asyncMapped, ["1", "2", "3"], "async map should stringify values");

  // -----------------------------------------------------------------------
  // Test 4: filter removes items
  // -----------------------------------------------------------------------
  const evens = await toArray(filter(range(1, 8), (n) => n % 2 === 0));
  assert.deepEqual(evens, [2, 4, 6, 8], "filter should keep only even numbers");

  // -----------------------------------------------------------------------
  // Test 5: batch groups items correctly
  // -----------------------------------------------------------------------
  const batches = await toArray(batch(range(1, 7), 3));
  assert.deepEqual(
    batches,
    [[1, 2, 3], [4, 5, 6], [7]],
    "batch(range(1,7), 3) should produce [[1,2,3],[4,5,6],[7]]"
  );

  // batch size larger than input — one batch with everything
  const oneBatch = await toArray(batch(range(1, 3), 100));
  assert.deepEqual(oneBatch, [[1, 2, 3]], "batch > length should produce one batch");

  // -----------------------------------------------------------------------
  // Test 6: composing map + filter + take
  // -----------------------------------------------------------------------
  // Take first 3 even squares from 1..100
  const pipeline = take(
    filter(
      map(range(1, 100), (n) => n * n),
      (n) => n % 2 === 0
    ),
    3
  );

  const composedResult = await toArray(pipeline);
  assert.deepEqual(composedResult, [4, 16, 36], "Composed pipeline: first 3 even squares");

  // -----------------------------------------------------------------------
  // Test 7: fromArray preserves order
  // -----------------------------------------------------------------------
  const words = ["alpha", "beta", "gamma", "delta"];
  const fromArr = await toArray(fromArray(words));
  assert.deepEqual(fromArr, words, "fromArray should preserve order");

  // -----------------------------------------------------------------------
  // Test 8: count without collecting
  // -----------------------------------------------------------------------
  const n = await count(range(1, 1000));
  assert.equal(n, 1000, "count should handle 1000 items without collecting");

  // -----------------------------------------------------------------------
  // Test 9: empty iterable edge cases
  // -----------------------------------------------------------------------
  const emptyArr: number[] = [];
  const emptyResult = await toArray(map(fromArray(emptyArr), (x) => x * 2));
  assert.deepEqual(emptyResult, [], "map over empty should yield empty");

  const emptyBatch = await toArray(batch(fromArray(emptyArr), 5));
  assert.deepEqual(emptyBatch, [], "batch over empty should yield empty");

  console.log("All tests passed!");
}

await main();
