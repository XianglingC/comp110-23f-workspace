"""Combing two lists into a dictionary"""
__author__ = "730658974"

# Part 1. zip()
def zip(x:list[str], y:list[int]) -> dict[str,int]:
    """Combining two list to a dictionary"""
    if len(x) != len(y) or len(x) == 0 or len(y) == 0:
        return {}
    #why {}doesn't work?
    else:
        zip_list: dict[str, int] = {}
        for i in range(len(x)):
            zip_list [x[i]] = y[1]
        return zip_list