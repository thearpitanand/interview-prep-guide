"""
Problem: Reverse String Using Stack (GFG) | Optional | Easy
Topic: Stacks and Queues

Reverse a string using a stack.

Example 1:
  Input: s = "hello"
  Output: "olleh"

Constraints:
  - 1 <= len(s) <= 10^4

Hint: Push all chars, pop all to build reversed string.
Pattern: Stack
"""


def reverse_string_stack(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert reverse_string_stack("hello") == "olleh"
    assert reverse_string_stack("a") == "a"
    assert reverse_string_stack("ab") == "ba"
    print("All tests passed!")
