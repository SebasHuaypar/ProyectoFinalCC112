# Implementar un programa que convierta entre diferentes monedas utilizando tasas de cambio predefinidas.

# Usaremos tkinter para hacer una interfaz más amigable, así que lo importamos primero.

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox


# Definimos mediante un diccionario las tasas de cambio.

tasasDeCambio = {
    'PEN': 1.0,
    'EUR': 0.25,
    'USD': 0.26,
    'BOB': 1.83,
    'MXN': 4.89
}

# Implementamos una función que nos permita realizar las conversiones.

def convertirMoneda(): 
    try:
        cantidad = float(ingresarCantidad.get())
        monedaOrigen = monedaOrigen_combobox.get()
        monedaDestino = monedaDestino_combobox.get()

        if monedaOrigen in tasasDeCambio and monedaDestino in tasasDeCambio:
            resultado = cantidad * (tasasDeCambio[monedaDestino] / tasasDeCambio[monedaOrigen])
            resultadoLabel.config(text=f'{resultado:.2f} {monedaDestino}')
        else:
            resultadoLabel.config(text="Moneda no registrada")
    except ValueError:
        messagebox.showerror("Error", "Ingrese una cantidad válida")

# # Creamos la ventana principal con tkinter.

ventanaPrincipal = tk.Tk() 
ventanaPrincipal.title("Conversor de Monedas")

# Definimos y diseñamos las entradas de texto.

ingresarCantidadLabel = tk.Label(ventanaPrincipal, text="Cantidad:") 
ingresarCantidadLabel.grid(row=0, column=0, padx=10, pady=10)

ingresarCantidad = tk.Entry(ventanaPrincipal)
ingresarCantidad.grid(row=0, column=1, padx=10, pady=10)

monedaOrigenLabel = tk.Label(ventanaPrincipal, text="De:")
monedaOrigenLabel.grid(row=1, column=0, padx=10, pady=10)

monedaOrigen_combobox = ttk.Combobox(ventanaPrincipal, values=list(tasasDeCambio.keys()))
monedaOrigen_combobox.grid(row=1, column=1, padx=10, pady=10)
monedaOrigen_combobox.current(0)

monedaDestinoLabel = tk.Label(ventanaPrincipal, text="A:")
monedaDestinoLabel.grid(row=2, column=0, padx=10, pady=10)

monedaDestino_combobox = ttk.Combobox(ventanaPrincipal, values=list(tasasDeCambio.keys()))
monedaDestino_combobox.grid(row=2, column=1, padx=10, pady=10)
monedaDestino_combobox.current(1)

# Creamos los botones para realizar la conversión y para salir del aplicativo.

tk.Button(ventanaPrincipal, text="Convertir", command=convertirMoneda) 
ventanaPrincipal.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tk.Button(ventanaPrincipal, text="Salir", command=ventanaPrincipal.destroy)
ventanaPrincipal.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Definimos y diseñamos el lugar donde se mostrará el resultado de la conversión.

resultadoLabel = tk.Label(ventanaPrincipal, text='Aquí aparecerá el resultado')
resultadoLabel.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


ventanaPrincipal.mainloop()
