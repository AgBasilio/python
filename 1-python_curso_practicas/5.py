"""5. Escriba un código que desordene al azar una lista."""

import random


def disorder(list):
    newList = []
    while len(list) > 0:
        index = random.randint(0, len(list) - 1)
        newList.append(list.pop(index))
    return newList


myList = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"Mi lista a desordenar {myList}, y la lista ya desordenada {disorder(myList)}")
