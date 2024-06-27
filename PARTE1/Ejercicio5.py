# Explicar cómo funcionan las referencias en Python y crear una función que demuestre la mutabilidad de las listas.

# En el caso de Python, al momento de asignar una variable a otra variable, lo que sucede es que ambas apuntarán al mismo objeto almacenado en memoria. Esto sucede debido a que las variables no contienen directamente los valores asignados sino referencias a los objetos que tienen esos valores.

# A continuación usaré un ejemplo donde podremos ver que una lista puede ser modificada sin tener que crear un nuevo objeto.

lista = ["Lentejas", "Papa", "Arvejas", "Pan", "Azucar"]

def mutabilidadLista(lista):
    print("Lista original: " + str(lista))

    lista.append("Agua") # Agregamos el elemento "Agua"  a la lista.

    print("Lista modificada: " + str(lista))

    lista.pop(2) # Eliminamos el elemento de índica 2 (3er elemento) de la lista.

    print("Lista modificada nuevamente: " + str(lista))

mutabilidadLista(lista)
