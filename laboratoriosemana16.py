import random

# 1. Mostrar el texto "Semana No. 16: Ejercicio 1"
print("Semana No. 16: Ejercicio 1")

# 2. Almacenar en un arreglo unidimensional 10 números generados aleatoriamente
arreglo = [random.randint(1, 100) for _ in range(10)]

# 3. Realizar las siguientes opciones:
# a. Mostrar los números ingresados
print(f"Números ingresados: {arreglo}")

# b. Mostrar el promedio del arreglo
promedio = sum(arreglo) / len(arreglo)
print(f"Promedio del arreglo: {promedio}")

# c. Mostrar la longitud del arreglo
print(f"Longitud del arreglo: {len(arreglo)}")

# d. Encontrar y mostrar:
# i. La suma de posiciones pares
suma_pares = sum(arreglo[i] for i in range(len(arreglo)) if i % 2 == 0)
print(f"Suma de posiciones pares: {suma_pares}")

# ii. La suma de posiciones impares
suma_impares = sum(arreglo[i] for i in range(len(arreglo)) if i % 2 != 0)
print(f"Suma de posiciones impares: {suma_impares}")

import random

# 1. Mostrar el texto "Semana No. 12: Ejercicio 2"
print("Semana No. 12: Ejercicio 2")

# 2. Solicitar al usuario las dimensiones de la matriz
filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

# 3. Poblar la matriz con números aleatorios entre 0 y 1000
matriz = [[random.randint(0, 1000) for _ in range(columnas)] for _ in range(filas)]

# 4. Indicar las siguientes estadísticas:
# a. Cantidad de números pares
pares = sum(1 for fila in matriz for num in fila if num % 2 == 0)
print(f"Cantidad de números pares: {pares}")

# b. Cantidad de números impares
impares = sum(1 for fila in matriz for num in fila if num % 2 != 0)
print(f"Cantidad de números impares: {impares}")

# c. Número mayor
mayor = max(num for fila in matriz for num in fila)
print(f"Número mayor: {mayor}")

# d. Número menor
menor = min(num for fila in matriz for num in fila)
print(f"Número menor: {menor}")
