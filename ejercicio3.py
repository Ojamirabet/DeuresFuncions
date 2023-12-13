def sumar_numeros(numeros, numero):
    suma = []
    for i in numeros:
        suma.append(i + numero)
    return suma
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numero = int(input("Dime el número que quieres sumar:"))
print(sumar_numeros(numeros, numero))
