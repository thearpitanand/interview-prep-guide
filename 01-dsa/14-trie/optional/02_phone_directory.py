"""
Problem: Phone Directory Using Trie (GFG) | Optional | Medium
Topic: Trie

Given a list of contacts, for each prefix typed, show all matching contacts.

Example 1:
  Input: contacts = ["gee", "geek", "geezer"], query = "gee"
  Output: [["gee","geek","geezer"], ["gee","geek","geezer"], ["gee","geek","geezer"]]

Constraints:
  - 1 <= n <= 10^4

Hint: Build trie. For each prefix, collect all words under that trie node.
Pattern: Trie + DFS
"""


def phone_directory(contacts: list[str], query: str) -> list[list[str]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = phone_directory(["gee", "geek", "geezer"], "gee")
    assert len(result) == 3
    assert "gee" in result[0]
    print("All tests passed!")
