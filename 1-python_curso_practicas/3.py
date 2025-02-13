"""Realizar una suma de los elementos de una tupla"""


def sum(tuple):
    total = 0
    for number in tuple:
        total += number
    return total


# tuple = [1, 32, 54, 723, 34, 543, 21, 10]
tuple = [1, 1, 1, 1, 1, 1, 1, 1]  # 8
assert sum(tuple) == 8
print("the sum is: ", sum(tuple))
