"""Summing the elements of a list using different loops."""
__author__ = "730658974"


# Version A: using the while loop
def w_sum(vals: list[float]) -> float:
    """Using the while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


# Version B: using the for...in...loop
def f_sum(vals: list[float]) -> float:
    """Using the for in loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


# Version C: using the for..in rang(len(xs))
# Now it's should be worked as the while loop
def f_range_sum(vals: list[float]) -> float:
    """Using for in range."""
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += vals[elem]
    return sum