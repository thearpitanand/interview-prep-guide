/**
 * Generic in-memory table with typed CRUD and query operations.
 * T must have an `id: string` field used as the primary key.
 */

export class Table<T extends { id: string }> {
  private store = new Map<string, T>();

  /**
   * Insert a new record. Throws if a record with the same id already exists.
   */
  insert(record: T): T {
    if (this.store.has(record.id)) {
      throw new Error(`Record with id "${record.id}" already exists.`);
    }
    this.store.set(record.id, { ...record });
    return record;
  }

  /**
   * Find a record by its primary key. Returns undefined if not found.
   */
  findById(id: string): T | undefined {
    return this.store.get(id);
  }

  /**
   * Merge patch into the existing record identified by id.
   * The `id` field cannot be patched.
   * Throws if the record does not exist.
   */
  update(id: string, patch: Partial<Omit<T, "id">>): T {
    const existing = this.store.get(id);
    if (existing === undefined) {
      throw new Error(`Record with id "${id}" not found.`);
    }
    const updated: T = { ...existing, ...patch };
    this.store.set(id, updated);
    return updated;
  }

  /**
   * Remove a record by id. Returns true if the record existed, false otherwise.
   */
  delete(id: string): boolean {
    return this.store.delete(id);
  }

  /**
   * Return all records that satisfy the predicate.
   */
  where(predicate: (record: T) => boolean): T[] {
    return Array.from(this.store.values()).filter(predicate);
  }

  /**
   * Return an array of the values at `key` for every record.
   * The return type is T[K][], precisely typed to the field.
   */
  pluck<K extends keyof T>(key: K): T[K][] {
    return Array.from(this.store.values()).map((record) => record[key]);
  }

  /**
   * Group all records by the string representation of the value at `key`.
   * Keys of the result are the distinct values seen in the table.
   */
  groupBy<K extends keyof T>(key: K): Record<string, T[]> {
    const result: Record<string, T[]> = {};
    for (const record of this.store.values()) {
      const groupKey = String(record[key]);
      if (result[groupKey] === undefined) {
        result[groupKey] = [];
      }
      result[groupKey].push(record);
    }
    return result;
  }

  /**
   * Total number of records in the table.
   */
  count(): number {
    return this.store.size;
  }

  /**
   * Return all records as an array (insertion order is not guaranteed).
   */
  all(): T[] {
    return Array.from(this.store.values());
  }
}
