# Inicializamos una lista vacía para almacenar las edades
edades = []

# Utilizamos un ciclo for para pedir al usuario que ingrese las edades
for i in range(5):
    while True:
        try:
            edad = int(input("Por favor, ingresa la edad de la persona " + str(i+1) + ": "))
            if edad < 0:
                print("La edad no puede ser un número negativo. Por favor, intenta de nuevo.")
            else:
                break
        except ValueError:
            print("La edad debe ser un número entero. Por favor, intenta de nuevo.")
    edades.append(edad)

# Mostramos en pantalla las edades ingresadas por el usuario
print("Las edades ingresadas son:")
for i, edad in enumerate (edades):
    print(f'edad {i+1}:{edad}')
