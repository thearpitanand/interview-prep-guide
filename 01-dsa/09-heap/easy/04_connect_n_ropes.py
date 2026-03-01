"""
Problem: Connect N Ropes with Min Cost (GFG) | Day 28 | Easy
Topic: Heap

Given N ropes of different lengths, connect them into one rope. The cost of
connecting two ropes is the sum of their lengths. Find the minimum total cost.

Example 1:
  Input: ropes = [4, 3, 2, 6]
  Output: 29  # Connect 2+3=5(cost 5), 4+5=9(cost 9), 6+9=15(cost 15) → total 29

Constraints:
  - 1 <= n <= 10^5
  - 1 <= ropes[i] <= 10^6

Hint: Always connect the two shortest ropes first. Use a min-heap.
Pattern: Min-Heap / Greedy
"""


def connect_ropes(ropes: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert connect_ropes([4, 3, 2, 6]) == 29
    assert connect_ropes([1, 2, 3]) == 9
    assert connect_ropes([5]) == 0
    print("All tests passed!")
