"""Test my zip function."""

__author__ = "730658974"

from lessons.zip import zip


# Use cases 1
def test_use_case_1() -> None:
    """Test first use cases."""
    string_list: list[str] = ["eggs", "milk"]
    int_list: list[int] = [1, 2]
    assert zip(string_list, int_list) == {"eggs": 1, "milk": 2}


# Use cases 2
def test_use_case_2() -> None:
    """Test second use cases."""
    str_list: list[str] = ["banana"]
    int_list: list[int] = [9]
    assert zip(str_list, int_list) == {"banana": 9}


# Edge case testing
def test_edge_case() -> None:
    """Test edge case with empty string list."""
    str_list: list[str] = []
    int_list: list[int] = [2, 3]
    assert zip(str_list, int_list) == {}