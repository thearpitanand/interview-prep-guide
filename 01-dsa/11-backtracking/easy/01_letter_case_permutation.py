"""
Letter Case Permutation (LC 784)

Day: 31 | Difficulty: Easy | Pattern: Backtracking

Given a string s, you can transform every letter individually to be lowercase
or uppercase to create another string. Return a list of all possible strings
we could create. Return the output in any order.

Examples:
    Input: s = "a1b2"
    Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    Input: s = "3z4"
    Output: ["3z4", "3Z4"]

    Input: s = "12345"
    Output: ["12345"]

Constraints:
    - 1 <= s.length <= 12
    - s consists of lowercase English letters, uppercase English letters, and digits

Hint:
    At each character position, if it's a letter you have two choices (lower/upper).
    If it's a digit, there's only one choice. Think of it as a binary tree where
    each letter position creates a branch.

Pattern: Backtracking - at each index, choose lowercase or uppercase for letters,
then recurse to the next index. Digits are added as-is.
"""

from typing import List


def letter_case_permutation(s: str) -> List[str]:
    """Generate all letter case permutations of the string."""
    pass


def letter_case_permutation_iterative(s: str) -> List[str]:
    """Iterative BFS-style approach - build results level by level."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Mixed letters and digits
    result = sorted(letter_case_permutation("a1b2"))
    expected = sorted(["a1b2", "a1B2", "A1b2", "A1B2"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: One letter with digits
    result = sorted(letter_case_permutation("3z4"))
    expected = sorted(["3z4", "3Z4"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 3: All digits - only one permutation
    result = letter_case_permutation("12345")
    assert result == ["12345"], f"Expected ['12345'], got {result}"

    # Test 4: Single letter
    result = sorted(letter_case_permutation("a"))
    expected = sorted(["a", "A"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 5: All letters
    result = sorted(letter_case_permutation("ab"))
    expected = sorted(["ab", "aB", "Ab", "AB"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 6: Iterative approach
    result = sorted(letter_case_permutation_iterative("a1b2"))
    expected = sorted(["a1b2", "a1B2", "A1b2", "A1B2"])
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")
