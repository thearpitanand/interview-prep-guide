/**
 * Generic in-memory table with typed CRUD and query operations.
 * T must have an `id: string` field used as the primary key.
 */

export class Table<T extends { id: string }> {
  private store: Map<string, T>;

  constructor() {
    // TODO
    this.store = new Map();
  }

  /**
   * Insert a new record. Throws if a record with the same id already exists.
   */
  insert(record: T): T {
    throw new Error("TODO: implement insert");
  }

  /**
   * Find a record by its primary key. Returns undefined if not found.
   */
  findById(id: string): T | undefined {
    throw new Error("TODO: implement findById");
  }

  /**
   * Merge patch into the existing record identified by id.
   * The `id` field cannot be patched.
   * Throws if the record does not exist.
   */
  update(id: string, patch: Partial<Omit<T, "id">>): T {
    throw new Error("TODO: implement update");
  }

  /**
   * Remove a record by id. Returns true if the record existed, false otherwise.
   */
  delete(id: string): boolean {
    throw new Error("TODO: implement delete");
  }

  /**
   * Return all records that satisfy the predicate.
   */
  where(predicate: (record: T) => boolean): T[] {
    throw new Error("TODO: implement where");
  }

  /**
   * Return an array of the values at `key` for every record.
   * The return type is T[K][], precisely typed to the field.
   */
  pluck<K extends keyof T>(key: K): T[K][] {
    throw new Error("TODO: implement pluck");
  }

  /**
   * Group all records by the string representation of the value at `key`.
   * Keys of the result are the distinct values seen in the table.
   */
  groupBy<K extends keyof T>(key: K): Record<string, T[]> {
    throw new Error("TODO: implement groupBy");
  }

  /**
   * Total number of records in the table.
   */
  count(): number {
    throw new Error("TODO: implement count");
  }

  /**
   * Return all records as an array (insertion order is not guaranteed).
   */
  all(): T[] {
    throw new Error("TODO: implement all");
  }
}
