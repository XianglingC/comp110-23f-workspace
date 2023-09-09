"""Right if my number is 10 and wrong if my number is not 10"""

my_number_string: str = input("Guess a number:")
my_number: int = int(my_number_string)
if my_number == int(10):
    print(str("Right"))
else:
    print(str("Wrong"))