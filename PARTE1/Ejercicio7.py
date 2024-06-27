# Crear una agenda telefónica utilizando diccionarios.

# Definimos el diccionario agendaTelefonica

agendaTelefonica = {
    'Maria' : 945945945,
    'Fatima' : 978978978,
    'Carla' : 969969969,
    'Oscar' : 921921921
}

print("Agenda original: " + str(agendaTelefonica))

agendaTelefonica['Alberto'] = 998998998 #Agregamos el nombre y celular de Alberto.
del agendaTelefonica['Maria'] # Eliminamos el contacto de María.
agendaTelefonica['Carla'] = 912912912 # Cambiamos el número de Carla.

print("Agenda modificada: " + str(agendaTelefonica))
