// table.ts — Pure ASCII table renderer. No dependencies.

type Row = Record<string, unknown>;

/**
 * Render an array of records as a plain-text ASCII table.
 * Column widths are computed from the widest value in each column.
 */
export function renderTable(rows: Row[]): string {
  if (rows.length === 0) return "(empty)\n";

  const firstRow = rows[0];
  if (firstRow === undefined) return "(empty)\n";

  const cols = Object.keys(firstRow);
  if (cols.length === 0) return "(empty)\n";

  // Compute column widths: max of header length and all cell value lengths
  const widths: number[] = cols.map(col => {
    const cellLengths = rows.map(r => String(r[col] ?? "").length);
    return Math.max(col.length, ...cellLengths);
  });

  function cell(value: string, colIndex: number): string {
    const w = widths[colIndex] ?? 0;
    return ` ${value.padEnd(w)} `;
  }

  const sep = "+" + widths.map(w => "-".repeat(w + 2)).join("+") + "+";
  const header = "|" + cols.map((c, i) => cell(c, i)).join("|") + "|";
  const dataRows = rows.map(
    r => "|" + cols.map((c, i) => cell(String(r[c] ?? ""), i)).join("|") + "|"
  );

  return [sep, header, sep, ...dataRows, sep].join("\n") + "\n";
}
