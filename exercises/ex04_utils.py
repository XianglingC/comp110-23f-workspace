"""The ex04 practice of list."""
__author__: str = "730658974"


# 1. all
def all(input_list: list[int], integer: int) -> bool:
    """To check whether all the int in lists are the same."""
    list_idx: int = 0
    if len(input_list) == 0:
        return False
    while list_idx < len(input_list):
        if input_list[list_idx] != integer:
            return False
        else:
            list_idx += 1
    return True


# 2. max
def max(input: list[int]) -> int:
    """To find the maximum number in the list."""
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List")
    list_idx: int = 1
    max_value = input[0]
    while list_idx < len(input):
        if max_value < input[list_idx]:
            max_value = input[list_idx]
        list_idx += 1
    return max_value


# 3. is_equal
# The implementation should not assume the lengths of each list are equal???
def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Find whether the number in lists are all the same."""
    idx_1: int = 0
    idx_2: int = 0
    response: bool = True
    if len(input1) != len(input2):
        return False
    while idx_1 < len(input1) and response:
        if input2[idx_2] == input1[idx_1]:
            response = True
            idx_1 += 1
            idx_2 += 1
        else:
            response = False
    return response