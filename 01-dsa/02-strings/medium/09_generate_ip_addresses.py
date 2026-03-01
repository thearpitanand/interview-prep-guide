"""
Problem: Restore IP Addresses (LC 93) | Day 10 | Medium
Topic: Strings

Given a string containing only digits, return all possible valid IP addresses
that can be formed by inserting dots.

Example 1:
  Input: s = "25525511135"
  Output: ["255.255.11.135", "255.255.111.35"]

Constraints:
  - 1 <= s.length <= 20
  - s consists of digits only

Hint: Backtrack with 4 segments; each segment is 0-255, no leading zeros (except "0").
Pattern: Backtracking
"""


def restore_ip_addresses(s: str) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = restore_ip_addresses("25525511135")
    assert set(result) == {"255.255.11.135", "255.255.111.35"}
    assert restore_ip_addresses("0000") == ["0.0.0.0"]
    assert restore_ip_addresses("101023") == sorted(restore_ip_addresses("101023"))  # just ensure it runs
    print("All tests passed!")
