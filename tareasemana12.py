print("Semana No. 12: Ejercicio 1")

def sumatoria(n):
    return sum(range(1, n+1))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def tablas_multiplicar():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("\n")

def numero_perfecto(n):
    suma = sum(i for i in range(1, n) if n % i == 0)
    return suma == n

while True:
    print("\nSeleccione una opción:")
    print("a. Sumatoria")
    print("b. Factorial")
    print("c. Tablas de Multiplicar")
    print("d. Número perfecto")
    print("e. Salir")
    opcion = input("Opción: ")

    if opcion.lower() == 'a':
        n = int(input("Ingrese un número entero positivo: "))
        print(f"La sumatoria de 1 hasta {n} es {sumatoria(n)}")
    elif opcion.lower() == 'b':
        n = int(input("Ingrese un número entero positivo: "))
        print(f"El factorial de {n} es {factorial(n)}")
    elif opcion.lower() == 'c':
        print("Tablas de multiplicar del 1 al 10:")
        tablas_multiplicar()
    elif opcion.lower() == 'd':
        n = int(input("Ingrese un número entero positivo: "))
        if numero_perfecto(n):
            print(f"{n} es un número perfecto.")
        else:
            print(f"{n} no es un número perfecto.")
    elif opcion.lower() == 'e':
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")