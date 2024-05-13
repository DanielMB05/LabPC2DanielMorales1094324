import random

print("Semana No.16 Ejercicio 1")

lista= []

for x in range (10):
    lista.append(random.randint(0,10))

opcion = "a"

while (opcion != "e"):
    print("Menú")
    print("a. mostrar num", "b. promedio", "c. longitud", "d. posicion", "e. salir")
    opcion = input("ingrese su opcion\n")

    match opcion:
        case "a":
            for x in range (len(lista)):
                print(f"No. {x}: {lista [x]}")
        case "b": 
            print("PROMEDIO")
            sumatoria = 0
            for x in range (len(lista)):
                sumatoria  += lista [x]
            promedio = sumatoria / len(lista)
            print(f"----promedio: {promedio}")

