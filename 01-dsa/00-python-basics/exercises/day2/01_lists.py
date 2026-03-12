"""
Exercise: Lists | Day 2
Topic: Python Collections

Practice list operations, slicing, and manipulation.

Instructions: Implement each function below.
"""


def second_largest(nums: list[int]) -> int:
    """Return the second largest number in the list.
    Assume list has at least 2 unique numbers.
    Do NOT use sort.
    """

    """
    # Attempt 1
    
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return nums[0]

    largest = float("-inf")
    num_dup = list(nums)
    second_largest = float("-inf")

    for num in nums:
        if largest < num:
            largest = num

    num_dup.remove(largest)

    for num in num_dup:
        if second_largest < num:
            second_largest = num

    return second_largest
    """

    largest = float("-inf")
    second_largest = float("-inf")

    for num in nums:
        if largest < num:
            second_largest = largest
            largest = num
        elif second_largest < num and num != largest:
            second_largest = num

    return second_largest


def rotate_left(nums: list[int], k: int) -> list[int]:
    """Rotate list left by k positions.
    Example: rotate_left([1,2,3,4,5], 2) -> [3,4,5,1,2]
    """
    left_list = list(nums)[k:]
    right_list = list(nums)[:k]

    # print(left_list + right_list)

    return left_list + right_list


def flatten(nested: list) -> list:
    """Flatten a nested list (one level deep).
    Example: flatten([[1,2],[3,4],[5]]) -> [1,2,3,4,5]
    """
    return [x for row in nested for x in row]


def chunk(lst: list, size: int) -> list[list]:
    """Split list into chunks of given size.
    Example: chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    """
    bits = []

    for i in range(0, len(lst), size):
        bits.append(lst[i : i + size])

    return bits


def remove_all(lst: list, value) -> list:
    """Remove all occurrences of value from list.
    Return new list, don't modify original.
    """
    result = []

    for item in lst:
        if item != value:
            result.append(item)

    return result


# --- Tests ---
if __name__ == "__main__":
    assert second_largest([3, 1, 4, 1, 5, 9]) == 5
    assert second_largest([1, 2]) == 1

    assert rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
    assert rotate_left([1, 2, 3], 0) == [1, 2, 3]

    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]

    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3], 3) == [[1, 2, 3]]

    assert remove_all([1, 2, 3, 2, 4], 2) == [1, 3, 4]
    print("All tests passed!")
