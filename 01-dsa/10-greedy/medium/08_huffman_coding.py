"""
Problem: Huffman Coding (GFG) | Day 30 | Medium
Topic: Greedy

Given a string of characters and their frequencies, build a Huffman Tree
and return the codes for each character.

Example 1:
  Input: chars = ['a', 'b', 'c', 'd', 'e', 'f'], freq = [5, 9, 12, 13, 16, 45]
  Output: Huffman codes (variable-length prefix codes)

Constraints:
  - 1 <= n <= 10^3

Hint: Use min-heap. Repeatedly extract two min freq nodes, create parent with sum freq.
Pattern: Min-Heap / Greedy
"""
import heapq


def huffman_codes(chars: list[str], freq: list[int]) -> dict[str, str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    codes = huffman_codes(['a', 'b', 'c', 'd', 'e', 'f'], [5, 9, 12, 13, 16, 45])
    # Verify prefix-free property and all chars have codes
    assert len(codes) == 6
    for c in ['a', 'b', 'c', 'd', 'e', 'f']:
        assert c in codes
        assert all(ch in '01' for ch in codes[c])
    # f should have shortest code (highest freq)
    assert len(codes['f']) <= len(codes['a'])
    print("All tests passed!")
