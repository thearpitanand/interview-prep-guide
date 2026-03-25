"""
Exercise: Big O Analysis | Day 4
Topic: Algorithm Complexity

Analyze the time complexity of given code snippets.

Instructions: Each function describes a code pattern. Return its Big O as a string.
"""


def nested_loop_complexity() -> str:
    """What is the time complexity of this code?

    for i in range(n):
        for j in range(n):
            total += i + j

    Return: "O(n^2)", "O(n)", "O(n log n)", or "O(1)"
    """
    pass


def two_sequential_loops_complexity() -> str:
    """What is the time complexity of this code?

    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

    Return: "O(n^2)", "O(n)", "O(2n)", or "O(1)"
    Hint: O(n) + O(n) = ?
    """
    pass


def dict_lookup_complexity() -> str:
    """What is the time complexity of this code?

    seen = set()
    for x in nums:           # n iterations
        if x in seen:         # set lookup
            return True
        seen.add(x)

    Return: "O(n^2)", "O(n)", "O(n log n)", or "O(1)"
    Hint: set lookup is O(1), inside a loop of n iterations.
    """
    pass


def sorted_then_scan_complexity() -> str:
    """What is the time complexity of this code?

    nums.sort()               # sort first
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True

    Return: "O(n^2)", "O(n)", "O(n log n)", or "O(log n)"
    Hint: sort is O(n log n), scan is O(n). Total = ?
    """
    pass


def binary_search_complexity() -> str:
    """What is the time complexity of binary search on a sorted array?

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    Return: "O(n)", "O(log n)", "O(n log n)", or "O(1)"
    """
    pass


def max_n_for_quadratic() -> int:
    """In a coding interview (assuming ~10^8 operations/sec),
    what is roughly the maximum input size where O(n^2) passes?

    Refer to the quick rules table:
    n <= 10       -> O(n!) ok
    n <= 20       -> O(2^n) ok
    n <= 500      -> O(n^3) ok
    n <= 5,000    -> O(n^2) ok
    n <= 100,000  -> O(n log n) needed

    Return: 500, 5000, 50000, or 100000
    """
    pass


def operations_lookup() -> dict:
    """Return a dict mapping operation names to their Big O complexity.
    Use the common operations table from the markdown.

    Required keys and their correct values:
    - "list_access_by_index" -> the complexity
    - "list_search" -> the complexity
    - "dict_search" -> the complexity
    - "list_append" -> the complexity
    - "list_insert_front" -> the complexity
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert nested_loop_complexity() == "O(n^2)"
    assert two_sequential_loops_complexity() == "O(n)"
    assert dict_lookup_complexity() == "O(n)"
    assert sorted_then_scan_complexity() == "O(n log n)"
    assert binary_search_complexity() == "O(log n)"
    assert max_n_for_quadratic() == 5000

    ops = operations_lookup()
    assert ops["list_access_by_index"] == "O(1)"
    assert ops["list_search"] == "O(n)"
    assert ops["dict_search"] == "O(1)"
    assert ops["list_append"] == "O(1)"
    assert ops["list_insert_front"] == "O(n)"

    print("All tests passed!")
