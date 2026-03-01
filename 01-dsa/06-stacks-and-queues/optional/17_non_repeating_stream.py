"""
Problem: First Non-Repeating Char in Stream (GFG) | Optional | Medium
Topic: Stacks and Queues

Given a stream of characters, find the first non-repeating character at
each point in the stream. Return '#' if all characters so far are repeating.

Example 1:
  Input: stream = "aabcbc"
  Output: "a#bbcc" → wait, "a" -> "a#" -> "a#b"... let me redo
  Stream: a -> a -> b -> c -> b -> c
  Output: ['a', '#', 'b', 'b', 'c', '#']

Constraints:
  - 1 <= len(stream) <= 10^5

Hint: Use queue + frequency map. Dequeue while front has freq > 1.
Pattern: Queue + HashMap
"""
from collections import deque


def first_non_repeating_stream(stream: str) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert first_non_repeating_stream("aabcbc") == ['a', '#', 'b', 'b', 'c', '#']
    assert first_non_repeating_stream("abc") == ['a', 'a', 'a']
    print("All tests passed!")
