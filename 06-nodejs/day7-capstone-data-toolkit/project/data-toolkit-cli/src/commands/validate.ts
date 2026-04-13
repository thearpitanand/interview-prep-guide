// commands/validate.ts — Handler for the `validate` subcommand.

import { readFile } from "../io/read.ts";
import { getSchema, availableSchemas } from "../schemas/index.ts";
import type { ValidateOptions } from "../args.ts";

interface ValidationResult {
  index: number;
  errors: string[];
}

export function runValidate(opts: ValidateOptions): void {
  const schema = getSchema(opts.schema);
  if (!schema) {
    process.stderr.write(
      `Error: unknown schema "${opts.schema}". Available: ${availableSchemas.join(", ")}\n`
    );
    process.exit(1);
  }

  const rows = readFile(opts.file, opts.input);
  const invalid: ValidationResult[] = [];
  let validCount = 0;

  for (const [i, row] of rows.entries()) {
    const result = schema.safeParse(row);
    if (result.success) {
      validCount++;
    } else {
      const errors = result.error.issues.map(
        issue => `[${issue.path.join(".") || "(root)"}] ${issue.message}`
      );
      invalid.push({ index: i, errors });
    }
  }

  const total = rows.length;

  process.stdout.write(`Schema:  ${opts.schema}\n`);
  process.stdout.write(`File:    ${opts.file}\n`);
  process.stdout.write(`Total:   ${total}\n`);
  process.stdout.write(`Valid:   ${validCount}\n`);
  process.stdout.write(`Invalid: ${invalid.length}\n`);

  if (invalid.length > 0) {
    process.stdout.write(`\nValidation errors:\n`);
    for (const { index, errors } of invalid) {
      process.stdout.write(`  Row ${index}:\n`);
      for (const err of errors) {
        process.stdout.write(`    ${err}\n`);
      }
    }
  }
}
