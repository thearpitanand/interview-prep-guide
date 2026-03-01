"""
Relative Ranks

Day: 28
Difficulty: Easy
Topic: Heap / Sort
Link: https://leetcode.com/problems/relative-ranks/
Pattern: Heap or Sort with Index Mapping

Description:
    You are given an integer array 'score' of size n, where score[i] is the
    score of the ith athlete in a competition. All the scores are guaranteed
    to be unique.

    The athletes are placed based on their scores, where the 1st place athlete
    has the highest score, the 2nd place athlete has the 2nd highest score,
    and so on. The placement of each athlete determines their rank:
        - The 1st place athlete's rank is "Gold Medal".
        - The 2nd place athlete's rank is "Silver Medal".
        - The 3rd place athlete's rank is "Bronze Medal".
        - For the 4th place to the nth place athlete, their rank is their
          placement number (i.e., the xth place athlete's rank is "x").

    Return an array answer of size n where answer[i] is the rank of the
    ith athlete.

Examples:
    Input: score = [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    Input: score = [10, 3, 8, 9, 4]
    Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

Constraints:
    - n == score.length
    - 1 <= n <= 10^4
    - 0 <= score[i] <= 10^6
    - All the values in score are unique.

Hint:
    Use a max-heap (negate values) storing (score, index) tuples. Pop elements
    one by one and assign ranks. Alternatively, sort indices by score in
    descending order.

Pattern:
    Heap/Sort - Use max-heap to process athletes from highest to lowest score
    and assign ranks in order.
"""

from typing import List


def find_relative_ranks(score: List[int]) -> List[str]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Descending order
    assert find_relative_ranks([5, 4, 3, 2, 1]) == [
        "Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"
    ], "Test 1 Failed"

    # Test 2: Random order
    assert find_relative_ranks([10, 3, 8, 9, 4]) == [
        "Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"
    ], "Test 2 Failed"

    # Test 3: Single athlete
    assert find_relative_ranks([100]) == ["Gold Medal"], "Test 3 Failed"

    # Test 4: Two athletes
    assert find_relative_ranks([1, 2]) == [
        "Silver Medal", "Gold Medal"
    ], "Test 4 Failed"

    # Test 5: Three athletes
    assert find_relative_ranks([3, 1, 2]) == [
        "Gold Medal", "Bronze Medal", "Silver Medal"
    ], "Test 5 Failed"

    print("All test cases passed!")
