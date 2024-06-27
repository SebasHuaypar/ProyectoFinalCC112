# Crear una función que calcule el factorial de un número.

def factorial(n):
    resultado = 1

    if n < 0:
        return "¡El factorial no está definido para números negativos!"

    elif n == 0:
        return 1

    while n > 0:
        resultado *= n
        n -= 1
    return resultado    

n = int(input("Ingrese un número para calcular su factorial: "))
print("El factorial de " + str(n) + " es: " + str(factorial(n)))
