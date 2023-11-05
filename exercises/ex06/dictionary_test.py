"""EX07 Unit Test Plus!"""

__author__ = "730658974"

# The Unit test for INVERT FUNCTION"
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# INVERT_TEST1
def test_invert_use_case_1() -> None:
    """Unit test1."""
    dict_1: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(dict_1) == {"z": "a", "y": "b", "x": "c"}


# INVERT_TEST2
def test_invert_use_case_2() -> None:
    """Unit test2."""
    dict_2: dict[str, str] = {"z": "a", "y": "b", "x": "c"}
    assert invert(dict_2) == {"a": "z", "b": "y", "c": "x"}


# INVERT_TEST3
def test_invert_edge_case() -> None:
    """Unit test3."""
    dict_3: dict[str, str] = {}
    assert invert(dict_3) == {}


# -------------------------------------------------------------
# The Unit test for FAVORITE_COLOR FUNCTION
# TEST1
def test_use_case1() -> None:
    """Unit test 4."""
    name_color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(name_color) == "blue"


# TEST2
def test_use_case2() -> None:
    """Unit test5."""
    name_color2: dict[str, str] = {"Mia": "white", "Stella": "pink", "Rachel": "white", "Gloria": "pink"}
    assert favorite_color(name_color2) == "white"


# TEST3
def test_edge_case() -> None:
    """Unit test6."""
    name_color3: dict[str, str] = {}
    assert favorite_color(name_color3) == ""


# ---------------------------------------------
# The Unit test for COUNT FUNCTION
# TEST1
def test_count_use_case1() -> None:
    """Unit test7."""
    list1: list[str] = ["Mom", "Dad", "Mom"]
    assert count(list1) == {"Mom": 2, "Dad": 1}


# TEST2
def test_count_use_case2() -> None:
    """Unit test8."""
    list2: list[str] = ["Mom", "Dad", "Mom", "Dad"]
    assert count(list2) == {"Mom": 2, "Dad": 2}


# TEST3
def test_count_edge_case() -> None:
    """Unit test9."""
    list3: list[str] = ()
    assert count(list3) == {}


# ------------------------------------
# The Unit test for ALPHABETIZER FUNCTION
# TEST1
def test_alphabetizer_use_case1() -> None:
    """Unit test10."""
    list1: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(list1) == {"c": ["cat", "car"], "a": ["apple", "angry"], "b": ["boy", "bad"]}


# TEST2
def test_alphabetizer_use_case2() -> None:
    """Unit tes11."""
    list2: list[str] = ["hello", "bye"]
    assert alphabetizer(list2) == {"h": ["hello"], "b": ["bye"]}


# TEST3
def test_alphabetizer_edge_case() -> None:
    """Unit test12."""
    list3: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(list3) == {"p": ["Python", "party"], "s": ["sugar"], "t": ["Turtle", "table"]}


# -------------------------------------------------------
# The Unit test for UPDATE ATTENDANCE FUNCTION
# TEST1
def test_update_attendance_use_case1() -> None:
    """Unit test13."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(attendance_log, "Tuesday", "Vrinda") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}


# TEST2
def test_update_attendance_use_case2() -> None:
    """Unit test14."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert update_attendance(attendance_log, "Wednesday", "Kaleb") == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Kaleb"]}


# TEST3
def test_update_attendance_edge_case() -> None:
    """Unit test15."""
    attendance_log: dict = {"Monday": ["Anna"]}
    assert update_attendance(attendance_log, "Monday", "Anna") == {"Monday": ["Anna"]}