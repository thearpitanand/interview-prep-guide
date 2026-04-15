// commands/validate.ts — Handler for the `validate` subcommand.

import { readFile } from "../io/read.ts";
import { getSchema, availableSchemas } from "../schemas/index.ts";
import type { ValidateOptions } from "../args.ts";

interface ValidationResult {
  index: number;
  errors: string[];
}

export function runValidate(opts: ValidateOptions): void {
  throw new Error("TODO: implement runValidate");
}
