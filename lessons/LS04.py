def mimic (my_words: str) -> str:
    """Given the string my_words, outputs the same string"""
    return my_words

#Calling it
mimic("hello")

print(mimic("hello"))

my_words: str = "hello"
response: str =mimic(my_words)
print (response)

#Mimic function_2
def mimic_letter(word: str, index: int) -> str:
    """input a string and an index and it returns the letter at that index"""
    if index <= len(word):
        #response: str = word[index]
        return word[index]
    else:
        #response: str = "Too high of an index"
        return ("Index too high")
    return response
#Calling function
print(mimic_letter("hello",0))
my_word: str = input("input a word:")
index_value: int = int(input("input an integer:"))
