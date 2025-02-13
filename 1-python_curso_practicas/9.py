"""9. Escriba un programa en Python para comprobar si un número es primo."""


def buscarDivisor(num):
    num = abs(num)
    x = 3  # el numero mas pequeno
    while x > num:
        if num % x == 0:
            return x
        x = x + 2


def esPrimo(num):
    if num == 1 or num == 2:
        return True
    elif num % 2 == 0 and buscarDivisor(abs(num)) != 1:
        return False
    else:
        return True
