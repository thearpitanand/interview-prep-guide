/**
 * Day 2 — Exercise 06: Generic Classes
 *
 * Implement a generic Box<T> with get/set/map and a generic Stack<T>
 * with push/pop/peek/size. Both must work under strict mode with no `any`.
 *
 * Run: npx tsx day2-generics-and-utility-types/exercises/06_generic_classes.ts
 */
import assert from "node:assert/strict";

// ---------- YOUR CODE / ANSWERS BELOW ----------

class Box<T> {
  private value: T;

  constructor(initial: T) {
    this.value = initial;
  }

  get(): T {
    return this.value;
  }

  set(newValue: T): void {
    this.value = newValue;
  }

  /**
   * Transform the contained value, returning a new Box of the result type.
   */
  map<U>(fn: (value: T) => U): Box<U> {
    return new Box(fn(this.value));
  }

  toString(): string {
    return `Box(${String(this.value)})`;
  }
}

class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }

  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }

  get size(): number {
    return this.items.length;
  }

  isEmpty(): boolean {
    return this.items.length === 0;
  }

  /**
   * Return a copy of all items as an array (bottom to top).
   */
  toArray(): T[] {
    return [...this.items];
  }
}

// ---------- TESTS ----------

// Box — number
const numBox = new Box(42);
assert.equal(numBox.get(), 42);

numBox.set(100);
assert.equal(numBox.get(), 100);

// Box — map changes the type
const strBox = numBox.map((n) => n.toFixed(2));
assert.equal(strBox.get(), "100.00");

// Box — map to a boolean
const boolBox = new Box("hello").map((s) => s.length > 3);
assert.equal(boolBox.get(), true);

// Box — string round-trip
const sBox = new Box("world");
assert.equal(sBox.get(), "world");
sBox.set("earth");
assert.equal(sBox.get(), "earth");

// Box — object value
const objBox = new Box({ x: 1, y: 2 });
assert.deepEqual(objBox.get(), { x: 1, y: 2 });

// Stack — empty state
const numStack = new Stack<number>();
assert.equal(numStack.size, 0);
assert.equal(numStack.isEmpty(), true);
assert.equal(numStack.peek(), undefined);
assert.equal(numStack.pop(), undefined);

// Stack — push and peek
numStack.push(10);
numStack.push(20);
numStack.push(30);
assert.equal(numStack.size, 3);
assert.equal(numStack.peek(), 30);
assert.equal(numStack.isEmpty(), false);

// Stack — pop LIFO order
assert.equal(numStack.pop(), 30);
assert.equal(numStack.pop(), 20);
assert.equal(numStack.size, 1);

// Stack — toArray preserves order
const strStack = new Stack<string>();
strStack.push("a");
strStack.push("b");
strStack.push("c");
assert.deepEqual(strStack.toArray(), ["a", "b", "c"]);

// Stack — pop until empty
assert.equal(strStack.pop(), "c");
assert.equal(strStack.pop(), "b");
assert.equal(strStack.pop(), "a");
assert.equal(strStack.isEmpty(), true);

console.log("All tests passed!");
