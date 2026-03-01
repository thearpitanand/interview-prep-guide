"""
Problem: First Bad Version (LC 278) | Day 12 | Easy
Topic: Searching and Sorting

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

You have an API bool isBadVersion(version) which returns whether version is bad.
Find the first bad version. You should minimize the number of calls to the API.

Example 1:
  Input: n = 5, bad = 4
  Output: 4
  Explanation: isBadVersion(3) -> false, isBadVersion(5) -> true,
               isBadVersion(4) -> true. So 4 is the first bad version.

Example 2:
  Input: n = 1, bad = 1
  Output: 1

Constraints:
  - 1 <= bad <= n <= 2^31 - 1

Hint: Binary search for the boundary between good and bad versions.
      Use the left < right variant to find the leftmost true.
Pattern: Binary Search (Boundary Finding)
"""


def first_bad_version(n: int, is_bad_version) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    # Test 1: n=5, bad=4
    assert first_bad_version(5, lambda v: v >= 4) == 4
    # Test 2: n=1, bad=1
    assert first_bad_version(1, lambda v: v >= 1) == 1
    # Test 3: n=10, bad=7
    assert first_bad_version(10, lambda v: v >= 7) == 7
    # Test 4: n=3, bad=1
    assert first_bad_version(3, lambda v: v >= 1) == 1
    print("All tests passed!")
