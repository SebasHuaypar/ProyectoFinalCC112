# Escribir y leer datos desde un archivo de texto.

# Creamos un archivo .txt con el nombre de AgendaTelefonica y lo abrimos.

with open('AgendaTelefonica.txt', 'w') as archivo:

    # Escribimos en el archivo los nombres de los contactos del ejercicio 7 para usarlo como ejemplo.

    archivo.write("AGENDA TELEFONICA\n\n")
    archivo.write("Maria: 945945945\n")
    archivo.write("Fatima: 978978978\n")
    archivo.write("Carla: 969969969\n")
    archivo.write("Oscar: 921921921\n")

# Abrimos el archivo y leemos los datos en él.

with open('AgendaTelefonica.txt', 'r') as archivo:
    lineas = archivo.readlines()

# Imprimimos cada linea del archivo, utilizaremos strip() para eliminar los saltos de línea extras.

for linea in lineas:
    print(linea.strip())