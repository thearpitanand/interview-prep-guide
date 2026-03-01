"""
Problem: Print Unique Rows in Boolean Matrix (GFG) | Optional | Medium
Topic: Trie

Given a binary matrix, print all unique rows.

Example 1:
  Input: mat = [[1,1,0,1],[1,0,0,1],[1,1,0,1]]
  Output: [[1,1,0,1],[1,0,0,1]]

Constraints:
  - 1 <= R, C <= 100

Hint: Insert each row into a trie. If row path is new (last node not marked), it's unique.
Pattern: Trie / Hashing
"""


def unique_rows(mat: list[list[int]]) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert unique_rows([[1,1,0,1],[1,0,0,1],[1,1,0,1]]) == [[1,1,0,1],[1,0,0,1]]
    assert unique_rows([[0,0],[0,0]]) == [[0,0]]
    print("All tests passed!")
