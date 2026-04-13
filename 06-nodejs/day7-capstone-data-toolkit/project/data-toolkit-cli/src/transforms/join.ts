// join.ts — Left and inner join for two arrays of records.

type Row = Record<string, unknown>;

export type JoinType = "inner" | "left";

/**
 * Parse a join key spec string of the form "leftKey=rightKey".
 */
export function parseJoinKeys(on: string): { leftKey: string; rightKey: string } {
  const idx = on.indexOf("=");
  if (idx === -1) {
    throw new Error(`Join --on spec must be in the form "leftKey=rightKey", got: "${on}"`);
  }
  const leftKey = on.slice(0, idx);
  const rightKey = on.slice(idx + 1);
  if (!leftKey || !rightKey) {
    throw new Error(`Invalid join keys: "${on}"`);
  }
  return { leftKey, rightKey };
}

/**
 * Join two arrays of records on specified keys.
 *
 * - "inner": only rows that have a match in both sides
 * - "left":  all rows from the left side; unmatched get null-filled right columns
 *
 * Matched rows are merged: right-side keys are prefixed with "right_" if they
 * conflict with left-side keys.
 */
export function joinRecords(
  left: Row[],
  right: Row[],
  leftKey: string,
  rightKey: string,
  type: JoinType = "left"
): Row[] {
  // Build a lookup map from rightKey value → right rows (supports multiple matches)
  const rightMap = new Map<string, Row[]>();
  for (const row of right) {
    const k = String(row[rightKey] ?? "");
    const existing = rightMap.get(k);
    if (existing) {
      existing.push(row);
    } else {
      rightMap.set(k, [row]);
    }
  }

  const result: Row[] = [];

  for (const leftRow of left) {
    const k = String(leftRow[leftKey] ?? "");
    const matches = rightMap.get(k);

    if (matches && matches.length > 0) {
      for (const rightRow of matches) {
        result.push(mergeRows(leftRow, rightRow));
      }
    } else if (type === "left") {
      result.push({ ...leftRow });
    }
    // inner join: skip if no match
  }

  return result;
}

function mergeRows(left: Row, right: Row): Row {
  const merged: Row = { ...left };
  for (const [k, v] of Object.entries(right)) {
    // Prefix conflicting keys from the right side
    const finalKey = k in left && k !== Object.keys(left)[0] ? `right_${k}` : k;
    merged[finalKey] = v;
  }
  return merged;
}
