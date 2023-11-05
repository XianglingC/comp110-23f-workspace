"""Quiz 2 Practice"""
def odd_and_even(x:list[int]) -> list[int]:
    """Return odd that have even index"""
    new_list: list[int] =[]
    for idx in range(0, len(x)):
        if idx % 2 == 0 and x[idx] % 2 == 1:
            new_list.append(x[idx])
    return new_list

def value_exists(x:dict[str, int], y: int) -> bool:
    """"""
    result: bool = False
    for key in x:
        if x[key] == y:
            result = True
    return result
test_dict:[str, int] = {"a":2,"b":4,"c":7,"d":1}
test_val: int =4
value_exists(test_dict, 5)

def short_words(x:list[str]) -> list[str]:
    """"""
    new_list: list[str] = []
    for words in x:
        if len(words) > 4:
            print(f"{words} is too long!")
        else:
            new_list.append(words)
    return new_list

my_list: list[str] = ["sun", "cloud", "sky"]
print(short_words(my_list))



