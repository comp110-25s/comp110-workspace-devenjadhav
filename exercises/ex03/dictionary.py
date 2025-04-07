"""Dictionary function implementations for EX03."""

__author__ = "730760482"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary."""
    result: dict[str, str] = {}
    for key in d:
        val = d[key]
        if val in result:
            raise KeyError(f"Duplicate value found when inverting: {val}")
        result[val] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts occurrences of strings in a list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the most frequent color from a dictionary."""
    color_counts = count(list(favorites.values()))
    max_color = ""
    max_count = 0
    for color in favorites.values():
        if color_counts[color] > max_count:
            max_color = color
            max_count = color_counts[color]
    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Groups words into bins based on string length."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
