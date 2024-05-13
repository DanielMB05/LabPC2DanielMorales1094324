# Inicializamos una lista vacía para almacenar los nombres
nombres = []

# Utilizamos un ciclo for para pedir al usuario que ingrese los nombres
for i in range(5):
    nombre = input("Por favor, ingresa el nombre de una persona "  ": ")
    nombres.append(nombre)

# Mostramos en pantalla los nombres ingresados por el usuario
print("Los nombres ingresados son:")
for i, nombre in enumerate (nombres):
    print(f'nombre {i+1}: {nombre}')


