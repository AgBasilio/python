"""1. Dados dos números, escriba un código Python para
encontrar el mínimo de estos dos números"""


def get_lower(a, b):
    return a if a < b else b


first_number = int(input("Enter a whole  number: "))
second_number = int(input("Enter another whole  number: "))

print("the lowest number is: ", get_lower(first_number, second_number))
