def contar_vocales(palabra, vocales):
    contador_vocales = 0
    for i in palabra.lower():
        if i in vocales:
            contador_vocales +=1
    return contador_vocales
vocales = "aeiou"
palabra = input("Dime una palabra: ")
numero_de_vocales = contar_vocales(palabra, vocales)
print ("La palabra " + palabra + " tiene " + str(numero_de_vocales) + " vocales")

