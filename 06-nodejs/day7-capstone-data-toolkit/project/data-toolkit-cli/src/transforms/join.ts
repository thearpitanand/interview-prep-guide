// join.ts — Left and inner join for two arrays of records.

type Row = Record<string, unknown>;

export type JoinType = "inner" | "left";

/**
 * Parse a join key spec string of the form "leftKey=rightKey".
 */
export function parseJoinKeys(on: string): { leftKey: string; rightKey: string } {
  throw new Error("TODO: implement parseJoinKeys");
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
  throw new Error("TODO: implement joinRecords");
}
