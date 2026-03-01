"""
Problem: Book Allocation / Painters Partition (GFG / LC 410) | Day 14 | Medium
Topic: Searching and Sorting

Given N books with pages[i] pages and M students, allocate books such that:
- Each student gets at least one book
- Books are allocated contiguously
- Minimize the maximum pages any student has to read

Example 1:
  Input: pages = [12, 34, 67, 90], m = 2
  Output: 113  # [12,34,67] and [90] => max=113

Constraints:
  - 1 <= N <= 10^5
  - 1 <= pages[i] <= 10^6
  - 1 <= M <= N

Hint: Binary search on answer. For a given max pages, greedily check if m students suffice.
Pattern: Binary Search on Answer
"""


def book_allocation(pages: list[int], m: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert book_allocation([12, 34, 67, 90], 2) == 113
    assert book_allocation([10, 20, 30, 40], 2) == 60
    assert book_allocation([10, 20, 30], 1) == 60
    print("All tests passed!")
