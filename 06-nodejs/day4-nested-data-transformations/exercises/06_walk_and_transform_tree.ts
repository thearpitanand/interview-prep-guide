/**
 * Exercise 06 — Walk and Transform Trees
 *
 * Topics: recursive tree traversal, mapTree (pre-order), findInTree (DFS),
 *         generic tree types, predicate functions
 *
 * Implements:
 *   mapTree(root, fn)         — apply fn to every node; return new tree
 *   findInTree(root, pred)    — depth-first search; return first match
 *
 * Tested on a nested product-category tree.
 */

import assert from "node:assert/strict";

// ---------------------------------------------------------------------------
// Type: generic tree node
// ---------------------------------------------------------------------------

export type CategoryNode = {
  id: string;
  name: string;
  level: number;
  children?: CategoryNode[];
};

// ---------------------------------------------------------------------------
// mapTree — pre-order: fn applied to node before recursing into children
// ---------------------------------------------------------------------------

export function mapTree(
  node: CategoryNode,
  fn: (node: CategoryNode) => CategoryNode
): CategoryNode {
  throw new Error("TODO: implement mapTree");
}

// ---------------------------------------------------------------------------
// findInTree — depth-first search; returns first node matching predicate
// ---------------------------------------------------------------------------

export function findInTree(
  node: CategoryNode,
  predicate: (node: CategoryNode) => boolean
): CategoryNode | undefined {
  throw new Error("TODO: implement findInTree");
}

// ---------------------------------------------------------------------------
// reduceTree — accumulate a value across every node (depth-first)
// ---------------------------------------------------------------------------

export function reduceTree<A>(
  node: CategoryNode,
  fn: (acc: A, node: CategoryNode) => A,
  initial: A
): A {
  throw new Error("TODO: implement reduceTree");
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

if (import.meta.url === `file://${process.argv[1]}`) {
  // Product category tree:
  //
  //   Electronics (L0)
  //   ├── Computers (L1)
  //   │   ├── Laptops (L2)
  //   │   └── Desktops (L2)
  //   └── Audio (L1)
  //       ├── Headphones (L2)
  //       └── Speakers (L2)

  const tree: CategoryNode = {
    id: "cat-1",
    name: "Electronics",
    level: 0,
    children: [
      {
        id: "cat-2",
        name: "Computers",
        level: 1,
        children: [
          { id: "cat-3", name: "Laptops",   level: 2 },
          { id: "cat-4", name: "Desktops",  level: 2 },
        ],
      },
      {
        id: "cat-5",
        name: "Audio",
        level: 1,
        children: [
          { id: "cat-6", name: "Headphones", level: 2 },
          { id: "cat-7", name: "Speakers",   level: 2 },
        ],
      },
    ],
  };

  // ---- findInTree ----

  // Find by id
  const laptops = findInTree(tree, n => n.id === "cat-3");
  assert.ok(laptops !== undefined, "Laptops not found");
  assert.equal(laptops.name, "Laptops");

  // Find by name
  const audio = findInTree(tree, n => n.name === "Audio");
  assert.ok(audio !== undefined, "Audio not found");
  assert.equal(audio.id, "cat-5");

  // Find root itself
  const root = findInTree(tree, n => n.level === 0);
  assert.equal(root?.id, "cat-1");

  // Find level-2 nodes — returns FIRST match (depth-first: Laptops before Desktops)
  const firstLeaf = findInTree(tree, n => n.level === 2);
  assert.equal(firstLeaf?.name, "Laptops");

  // Not found → undefined
  const missing = findInTree(tree, n => n.id === "nonexistent");
  assert.equal(missing, undefined);

  // ---- mapTree — uppercase all names ----

  const uppercased = mapTree(tree, node => ({ ...node, name: node.name.toUpperCase() }));

  assert.equal(uppercased.name, "ELECTRONICS");          // root transformed
  assert.equal(tree.name, "Electronics");                // original unchanged

  const uppercasedLaptops = findInTree(uppercased, n => n.id === "cat-3");
  assert.equal(uppercasedLaptops?.name, "LAPTOPS");

  // All nodes should be uppercased
  const allNames = reduceTree(uppercased, (acc, n) => [...acc, n.name], [] as string[]);
  assert.ok(allNames.every(n => n === n.toUpperCase()), "Some names not uppercased");

  // ---- mapTree — increment level on every node ----

  const shifted = mapTree(tree, node => ({ ...node, level: node.level + 10 }));
  assert.equal(shifted.level, 10);

  const shiftedLeaf = findInTree(shifted, n => n.id === "cat-7");
  assert.equal(shiftedLeaf?.level, 12); // was 2, now 12

  // ---- reduceTree — collect all ids ----

  const allIds = reduceTree(tree, (acc, n) => [...acc, n.id], [] as string[]);
  assert.equal(allIds.length, 7); // 7 nodes total
  assert.ok(allIds.includes("cat-1"));
  assert.ok(allIds.includes("cat-7"));

  // ---- reduceTree — count nodes at a specific level ----

  const leafCount = reduceTree(tree, (acc, n) => acc + (n.level === 2 ? 1 : 0), 0);
  assert.equal(leafCount, 4); // Laptops, Desktops, Headphones, Speakers

  // ---- Single-node tree ----

  const single: CategoryNode = { id: "solo", name: "Solo", level: 0 };
  assert.equal(findInTree(single, n => n.id === "solo")?.name, "Solo");
  assert.equal(findInTree(single, n => n.level === 99), undefined);

  const mappedSingle = mapTree(single, n => ({ ...n, name: "SOLO" }));
  assert.equal(mappedSingle.name, "SOLO");
  assert.equal(mappedSingle.children, undefined);

  // ---- mapTree does not mutate the original ----

  // Deep-check that tree is unchanged after mapTree
  assert.equal(tree.name,                  "Electronics");
  assert.equal(tree.children?.[0]?.name,  "Computers");
  assert.equal(tree.children?.[1]?.name,  "Audio");
  assert.equal(
    tree.children?.[0]?.children?.[0]?.name,
    "Laptops"
  );

  console.log("All tests passed!");
}
