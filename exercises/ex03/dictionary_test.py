"""Unit tests for dictionary functions."""

__author__ = "730760482"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len
import pytest


# --- Tests for invert ---
def test_invert_use_case():
    """Basic invert test with unique values."""
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_single_pair():
    """Inverts a dictionary with one key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_keyerror():
    """Raises KeyError when duplicate values exist in input."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


# --- Tests for count ---
def test_count_normal():
    """Counts repeated items correctly."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_empty():
    """Returns empty dictionary when input is empty."""
    assert count([]) == {}


def test_count_one_item():
    """Counts one element correctly."""
    assert count(["x"]) == {"x": 1}


# --- Tests for favorite_color ---
def test_favorite_color_basic():
    """Returns the most common color."""
    data = {"Marc": "blue", "Ezri": "blue", "Kris": "green"}
    assert favorite_color(data) == "blue"


def test_favorite_color_tie():
    """Returns the first color in tie cases."""
    data = {"A": "red", "B": "blue", "C": "red", "D": "blue"}
    assert favorite_color(data) == "red"


def test_favorite_color_single():
    """Handles dictionary with one color."""
    assert favorite_color({"A": "green"}) == "green"


# --- Tests for bin_len ---
def test_bin_len_basic():
    """Bins by string length."""
    result = bin_len(["the", "quick", "fox"])
    assert result == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_duplicates():
    """Handles duplicates correctly using sets."""
    result = bin_len(["the", "the", "fox"])
    assert result == {3: {"the", "fox"}}


def test_bin_len_empty():
    """Handles empty list input."""
    assert bin_len([]) == {}
