// read.ts — Read JSON, NDJSON, and CSV files into typed arrays.

import { readFileSync } from "node:fs";
import { parse as parseCSV } from "csv-parse/sync";
import type { InputFormat } from "../args.ts";

type Row = Record<string, unknown>;

/**
 * Read a file and parse it into an array of records.
 * Throws on I/O errors or parse failures.
 */
export function readFile(filePath: string, format: InputFormat): Row[] {
  const raw = readFileSync(filePath, "utf8");

  switch (format) {
    case "json":
      return parseJSON(raw, filePath);
    case "ndjson":
      return parseNDJSON(raw, filePath);
    case "csv":
      return parseCSVContent(raw, filePath);
    default: {
      const _exhaustive: never = format;
      throw new Error(`Unknown format: ${String(_exhaustive)}`);
    }
  }
}

function parseJSON(raw: string, filePath: string): Row[] {
  let parsed: unknown;
  try {
    parsed = JSON.parse(raw);
  } catch (e) {
    throw new Error(`Failed to parse JSON from "${filePath}": ${String(e)}`);
  }

  if (!Array.isArray(parsed)) {
    throw new Error(`Expected a JSON array in "${filePath}", got ${typeof parsed}`);
  }

  return parsed.map((item, i) => {
    if (typeof item !== "object" || item === null || Array.isArray(item)) {
      throw new Error(`Item at index ${i} in "${filePath}" is not an object`);
    }
    return item as Row;
  });
}

function parseNDJSON(raw: string, filePath: string): Row[] {
  const lines = raw.split("\n").filter(line => line.trim() !== "");
  return lines.map((line, i) => {
    let parsed: unknown;
    try {
      parsed = JSON.parse(line);
    } catch (e) {
      throw new Error(`Failed to parse NDJSON line ${i + 1} in "${filePath}": ${String(e)}`);
    }
    if (typeof parsed !== "object" || parsed === null || Array.isArray(parsed)) {
      throw new Error(`NDJSON line ${i + 1} in "${filePath}" is not an object`);
    }
    return parsed as Row;
  });
}

function parseCSVContent(raw: string, filePath: string): Row[] {
  try {
    const records = parseCSV(raw, {
      columns: true,
      skip_empty_lines: true,
      trim: true,
    }) as Row[];
    return records;
  } catch (e) {
    throw new Error(`Failed to parse CSV from "${filePath}": ${String(e)}`);
  }
}
