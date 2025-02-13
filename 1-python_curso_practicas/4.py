"""4. Escriba un código que calcule una lista de números proporcionados."""

print('ingrese los numeros que quiera sumar, cunado quiera ver el total ingrese "q"')
total = 0
userInput = input()
while userInput != "q":
    total += int(userInput)
    print("La suma parcial es:", total)
    userInput = input("Ingrese otro numero: ")
print("La suma total es:", total)
