/**
 * Exercise 01 — Recursive Tree Types
 *
 * Topics: recursive type definitions, tree traversal, base-case thinking
 *
 * Tasks:
 *   1. Define `JsonValue` — a recursive type covering all valid JSON.
 *   2. Define `FSNode` — a file-system tree node (files and directories).
 *   3. Implement `countNodes(root)` — total node count including root.
 *   4. Implement `depth(root)` — longest root-to-leaf path length.
 *
 * Pattern: check for the leaf (base case) first, then reduce/map over children.
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// 1. JSON value type (self-referential)
// ---------------------------------------------------------------------------

type JsonPrimitive = string | number | boolean | null;
type JsonArray = JsonValue[];
type JsonObject = { [key: string]: JsonValue };
export type JsonValue = JsonPrimitive | JsonArray | JsonObject;

// ---------------------------------------------------------------------------
// 2. File-system tree node
// ---------------------------------------------------------------------------

export type FSNode = {
  name: string;
  type: "file" | "directory";
  size?: number;        // bytes; only meaningful for files
  children?: FSNode[];  // only directories have children
};

// ---------------------------------------------------------------------------
// 3. countNodes — total number of nodes in the tree (inclusive of root)
// ---------------------------------------------------------------------------

export function countNodes(root: FSNode): number {
  if (root.children === undefined || root.children.length === 0) {
    return 1;
  }
  return 1 + root.children.reduce((sum, child) => sum + countNodes(child), 0);
}

// ---------------------------------------------------------------------------
// 4. depth — length of the longest root-to-leaf path
//    A single-node tree has depth 1.
// ---------------------------------------------------------------------------

export function depth(root: FSNode): number {
  if (root.children === undefined || root.children.length === 0) {
    return 1;
  }
  return 1 + Math.max(...root.children.map(depth));
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  // --- JsonValue: verify a few values are assignable ---
  const _j1: JsonValue = 42;
  const _j2: JsonValue = "hello";
  const _j3: JsonValue = null;
  const _j4: JsonValue = [1, "two", { three: 3 }];
  const _j5: JsonValue = { nested: { deeply: [true, false] } };
  void _j1; void _j2; void _j3; void _j4; void _j5;

  // --- Build a sample file-system tree ---
  //
  //   root/              (directory)
  //   ├── readme.txt     (file)
  //   ├── src/           (directory)
  //   │   ├── index.ts   (file)
  //   │   └── utils.ts   (file)
  //   └── dist/          (directory)
  //       └── index.js   (file)

  const tree: FSNode = {
    name: "root",
    type: "directory",
    children: [
      { name: "readme.txt", type: "file", size: 1024 },
      {
        name: "src",
        type: "directory",
        children: [
          { name: "index.ts",  type: "file", size: 2048 },
          { name: "utils.ts",  type: "file", size: 512  },
        ],
      },
      {
        name: "dist",
        type: "directory",
        children: [
          { name: "index.js", type: "file", size: 4096 },
        ],
      },
    ],
  };

  // Nodes: root(1) + readme(1) + src(1) + index.ts(1) + utils.ts(1) + dist(1) + index.js(1) = 7
  assert.equal(countNodes(tree), 7);

  // Single node
  const single: FSNode = { name: "solo.txt", type: "file" };
  assert.equal(countNodes(single), 1);

  // Empty directory
  const emptyDir: FSNode = { name: "empty", type: "directory", children: [] };
  assert.equal(countNodes(emptyDir), 1);

  // depth: root(1) → src(2) → index.ts(3) = longest path of 3
  assert.equal(depth(tree), 3);
  assert.equal(depth(single), 1);
  assert.equal(depth(emptyDir), 1);

  // Deeper tree: 4 levels
  const deep: FSNode = {
    name: "a",
    type: "directory",
    children: [
      {
        name: "b",
        type: "directory",
        children: [
          {
            name: "c",
            type: "directory",
            children: [{ name: "d.txt", type: "file" }],
          },
        ],
      },
    ],
  };
  assert.equal(depth(deep), 4);
  assert.equal(countNodes(deep), 4);

  // Tree where one branch is deeper than another
  const uneven: FSNode = {
    name: "root",
    type: "directory",
    children: [
      { name: "shallow.txt", type: "file" },
      {
        name: "deep",
        type: "directory",
        children: [{ name: "leaf.txt", type: "file" }],
      },
    ],
  };
  assert.equal(depth(uneven), 3);   // root → deep → leaf
  assert.equal(countNodes(uneven), 4);

  console.log("All tests passed!");
}
