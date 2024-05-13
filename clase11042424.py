opcion = int(input("Sistema de números, 1. Un numero entre 1 y 5, 2. Ver Tablas de multiplicar, 3. Salir"))
contador = 0
numeros = []
numero_mayor = 0
match opcion:
    case "1":
        while (contador < 5):
            numero = int(input("Ingrese un número entero\n"))
            contador += 1
            numeros.append(numero)
            numero_mayor = max(numeros)
            print(f"El número mayor es :", numero_mayor)
        
     
    case "2":
        tituloCol = "\t"
        for col in range(1, 11):
            tituloCol += str(col) + "\t"
        print(tituloCol)

        textoFila = ""
        for fila in range(1,11):
            textoFila += str(fila) + "\t"

            for col in range(1, 11):
                textoFila += str(fila * col) + "\t"

            print(textoFila)
            textoFila = ""

    case "3":
        print("Adios")