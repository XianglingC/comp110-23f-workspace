"""Dictionary practice."""
__author__ = "730658974"


# Function1: invert
def invert(x: dict[str, str]) -> dict[str, str]:
    """The key list of input list becomes the values of the output list and vice versa."""
    new_dict: dict[str, str] = {}
    for key in x:
        value: str = x[key]
        if value in new_dict:
            raise KeyError("error message of your choice here!")
        new_dict[value] = key
    return new_dict


# Favorite colors
def favorite_color(names_colors: dict[str, str]) -> str:
    """Compare the frequency of the color in the dict."""
    color_num: dict[str, int] = {}
    for name in names_colors:
        color = names_colors[name]
        if color not in color_num:
            color_num[color] = 1
        else:
            color_num[color] += 1
    count: int = 0
    most_color: str = "" 
    for color in color_num:
        if color_num[color] > count:
            count = color_num[color]
            most_color = color
    return most_color


# Count
def count(counter: list[str]) -> dict[str, int]:
    """Return the number of apperence."""
    store: dict[str, int] = {}
    for item in counter:
        if item in store:
            store[item] += 1
        else:
            store[item] = 1
    return store
            

# Alphabetizer
def alphabetizer(str_list: list[str]) -> dict[str, list[str]]:
    """Sort the words in list with the same capital letter."""
    new_dict: dict[str, list[str]] = {}
    for elem in str_list:
        if elem[0].lower() not in new_dict:
            new_dict[elem[0]] = [elem]  # Create a new list with elem as its first element
        else:
            new_dict[elem[0].lower()].append(elem)  # Append elem to the existing list in new_dict
    return new_dict


# Update attendance
def update_attendance(x: dict[str, list[str]], day_of_week: str, attendance: str) -> dict[str, list[str]]:
    """Update attendance."""
    if day_of_week not in x:
        x[day_of_week] = [attendance]
    else:
        x[day_of_week].append(attendance)
    return x
