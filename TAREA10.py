print ("Semana No. 10 : Ejercicio 1")
mesEntrada = int(input("Ingrese un número del 1 al 12"))
mesSalida = ""

match mesEntrada:
    case 1: 
        mesSalida = "Enero"
    case 2:
        mesSalida = "Febrero"   
    case 3:
        mesSalida = "Marzo"
    case 4: 
        mesSalida = "Abril"
    case 5: 
        mesSalida = "Mayo"
    case 6: 
        mesSalida = "Junio"
    case 7: 
        mesSalida = "Julio"
    case 8: 
        mesSalida = "Agosto"
    case 9:
        mesSalida = "Septiembre"
    case 10:
        mesSalida = "Octubre"
    case 11: 
        mesSalida = "Noviembre"
    case 12: 
        mesSalida = "Diciembre"
    case _:
        mesSalida = "Error: cualquier número mayor a 12 no es admitido"

print ("MES:", mesSalida)
print (f"MES: {mesSalida}")



print("Semana No. 10: Ejercicio 3")
def main():
  A = int(input("Introduzca el primer número: "))
  B = int(input("Introduzca el segundo número: "))
  C = int(input("Introduzca el tercer número: "))

  if A <= 0 or B <= 0 or C <= 0:
    print("Error: Los números deben ser mayores a cero.")
  
  if A >= B and A >= C:
    if B == C:
      print("Los números", A, "y", B, "son los mayores.")
    else:
      print("El número", A, "es el mayor.")
  elif B >= A and B >= C:
    if A == C:
      print("Los números", B, "y", A, "son los mayores.")
    else:
      print("El número", B, "es el mayor.")
  else:
    if A == B:
      print("Los números", C, "y", A, "son los mayores.")
    else:
      print("El número", C, "es el mayor.")

if __name__ == "__main__":
  main()