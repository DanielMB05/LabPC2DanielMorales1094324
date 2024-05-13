def ObtenerAreaTriangulo(base, altura):
    return (base * altura) / 2

def ObtenerAreaCuadrado(lado):
    return lado ** 2

def ObtenerAreaRectangulo(base, altura):
    return base * altura

def ObtenerAreaCirculo(radio):
    pi = 3.14159
    return pi * (radio ** 2)

def main():
    print("Semana No. 12: Ejercicio 1")
    print("Seleccione la opción que desea calcular:")
    print("a. Área de triángulo")
    print("b. Área de cuadrado")
    print("c. Área de rectángulo")
    print("d. Área de círculo")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == 'a':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        print("El área del triángulo es: ", ObtenerAreaTriangulo(base, altura))
    elif opcion == 'b':
        lado = float(input("Ingrese el lado del cuadrado: "))
        print("El área del cuadrado es: ", ObtenerAreaCuadrado(lado))
    elif opcion == 'c':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        print("El área del rectángulo es: ", ObtenerAreaRectangulo(base, altura))
    elif opcion == 'd':
        radio = float(input("Ingrese el radio del círculo: "))
        print("El área del círculo es: ", ObtenerAreaCirculo(radio))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

print("Ejercicio 2")

x=0
y=0

def MoverPosicion(cantX, cantY):
    global x, y
    x += cantX
    y += cantY
opcion= 'a'
while(opcion != 'e'):
    print("Menú")
    print("a.SUBE", "b.BAJA","c.IZQUIERDA", "d.DERECHA", "e:SALIR", sep= "\t\n")
    opcion=input("ingrese su opción: ")

    match opcion:
        case 'a':
            MoverPosicion(0,1)
        case 'b':
            MoverPosicion(0,-1)
        case 'c':
            MoverPosicion(-1,0)
        case 'd':
            MoverPosicion(1,0)
        case _:
            print("Error: debe de ingresar una letra a-e")

    print(f"La posicion actual es: [{x}][{y}]")