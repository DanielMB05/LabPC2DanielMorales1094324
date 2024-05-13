print("semana No.11 Ejercicio 1")
n = int(input("ingrese un numero mayor a 0"))

if( n <= 0 ):
    print ("error, debe ser mayor a cero")

a=0
b=1
c=0

i=2
resultado=""

if ( n > 0 ):
    resultado = str(a)
    if (n>1):
        resultado = resultado + "," + str (b) 

        while (i < n):
            c= a + b
            resultado = resultado + "," + str (c) 
            a = b
            b = c
            i = i + 1

        print(resultado)
else:
    print(resultado)

#Ejercicio 2.A
print("Semana No. 11 Ejercicio 2")
n2 = int(input("ingrese un numero mayor a 0"))
if (n2<=0):
    print("ERROR")

calculoA = 0
for xA in range (1,n2,+1):
    calculoA += 1 / xA
print("El resultado de A es:", calculoA)

#Ejercicio 2.B





