"""
Exercise: Dicts and Sets | Day 2
Topic: Python Collections

Practice dictionary and set operations.

Instructions: Implement each function below.
"""


def word_frequency(text: str) -> dict[str, int]:
    """Count frequency of each word (lowercase).
    Example: word_frequency("the cat and the dog") -> {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
    """
    pass


def merge_dicts(d1: dict, d2: dict) -> dict:
    """Merge two dicts. If key exists in both, sum the values.
    Example: merge_dicts({'a': 1}, {'a': 2, 'b': 3}) -> {'a': 3, 'b': 3}
    """
    pass


def unique_elements(lst: list) -> list:
    """Return unique elements preserving order.
    Example: unique_elements([3, 1, 2, 1, 3]) -> [3, 1, 2]
    """
    pass


def common_elements(lst1: list, lst2: list) -> list:
    """Return sorted list of common elements.
    Example: common_elements([1,2,3], [2,3,4]) -> [2, 3]
    """
    pass


def invert_dict(d: dict) -> dict:
    """Swap keys and values.
    Example: invert_dict({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}
    """
    pass


# --- Tests ---
if __name__ == "__main__":
    assert word_frequency("the cat and the dog") == {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}

    assert merge_dicts({'a': 1}, {'a': 2, 'b': 3}) == {'a': 3, 'b': 3}

    assert unique_elements([3, 1, 2, 1, 3]) == [3, 1, 2]

    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]

    assert invert_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
    print("All tests passed!")
