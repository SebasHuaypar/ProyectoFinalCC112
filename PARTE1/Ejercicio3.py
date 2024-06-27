# Escribir una función que invierta una cadena.

# Forma 1: Utilizando la técnica del slicing [inicio:final:paso].

def invertirCadena1(cadena):
    return cadena[::-1]

cadena = str(input("Ingrese una cadena de texto a invertir: "))
print("Forma invertida: " + str(invertirCadena1(cadena)))

# Forma 2: Utilizando ciclo for para iterar sobre la cadena original y colocarlos de forma inversa en una nueva.

def invertirCadena2(cadena):
    cadena_invertida = ""

    for letra in cadena:
        cadena_invertida = letra + cadena_invertida
    return cadena_invertida

cadena = str(input("Ingrese una cadena de texto a invertir: "))
print("Forma invertida: " + str(invertirCadena2(cadena)))