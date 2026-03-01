"""
Problem: Count and Say (LC 38) | Day 10 | Medium
Topic: Strings

The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:
  - countAndSay(1) = "1"
  - countAndSay(n) is the run-length encoding of countAndSay(n - 1).

Run-length encoding (RLE) is a string compression method that works by
replacing consecutive identical characters with the count followed by
the character. For example, "3322251" is compressed as "23321511"
(two 3's, two 2's, one 5, one 1).

Example 1:
  Input: n = 1
  Output: "1"

Example 2:
  Input: n = 4
  Output: "1211"
  Explanation:
    countAndSay(1) = "1"
    countAndSay(2) = "11"       (one 1)
    countAndSay(3) = "21"       (two 1s)
    countAndSay(4) = "1211"     (one 2, then one 1)

Constraints:
  - 1 <= n <= 30

Hint: Iteratively build each term from the previous one. For each term,
      scan through counting consecutive identical digits, then append
      count + digit to build the next term.
Pattern: Simulation
"""


def count_and_say(n: int) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_and_say(1) == "1"
    assert count_and_say(2) == "11"
    assert count_and_say(3) == "21"
    assert count_and_say(4) == "1211"
    assert count_and_say(5) == "111221"
    assert count_and_say(6) == "312211"
    print("All tests passed!")
