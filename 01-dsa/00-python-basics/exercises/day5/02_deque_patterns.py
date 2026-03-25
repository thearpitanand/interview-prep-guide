"""
Exercise: Deque Patterns | Day 5
Topic: collections.deque

Practice O(1) operations on both ends, BFS pattern, and deque utilities.

Instructions: Implement each function below.
"""

from collections import deque


def bfs_level_order(graph: dict[int, list[int]], start: int) -> list[int]:
    """Return nodes in BFS visit order starting from start using deque.
    Use the BFS pattern from the markdown: popleft to dequeue, append to enqueue.
    Skip already-visited nodes.
    Example: bfs_level_order({0: [1, 2], 1: [3], 2: [3], 3: []}, 0) -> [0, 1, 2, 3]
    """
    pass


def rotate_array(nums: list[int], k: int) -> list[int]:
    """Rotate array to the right by k steps using deque.
    Use deque's O(1) pop() and appendleft().
    Example: rotate_array([1,2,3,4,5], 2) -> [4,5,1,2,3]
    """
    pass


def palindrome_check(s: str) -> bool:
    """Check if string is a palindrome using deque.
    Load characters into deque, then pop from both ends and compare.
    Ignore non-alphanumeric characters, case-insensitive.
    Example: palindrome_check("racecar") -> True
    Example: palindrome_check("hello") -> False
    """
    pass


def process_queue(arrivals: list[str], k: int) -> list[str]:
    """Simulate a queue where first k people are served (dequeued from left),
    and the rest leave (dequeued from right).
    Return the list of served people in order.
    Example: process_queue(["A","B","C","D","E"], 3) -> ["A","B","C"]
    Example: process_queue(["A","B"], 5) -> ["A","B"]
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert bfs_level_order({0: [1, 2], 1: [3], 2: [3], 3: []}, 0) == [0, 1, 2, 3]
    assert bfs_level_order({0: [1], 1: [2], 2: []}, 0) == [0, 1, 2]

    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_array([1, 2, 3], 0) == [1, 2, 3]

    assert palindrome_check("racecar") == True
    assert palindrome_check("hello") == False
    assert palindrome_check("A man a plan a canal Panama".replace(" ", "")) == True

    assert process_queue(["A", "B", "C", "D", "E"], 3) == ["A", "B", "C"]
    assert process_queue(["A", "B"], 5) == ["A", "B"]

    print("All tests passed!")
