print('--- Incio del programa ---')
nombre_cliente = input('Ingrese su nombre: ')
nit_cliente = int(input('Ingrese su NIT: '))

tamanio = 'Mediano'
precio = 20.00
azucar = 0
agrandado = False
i = 0
print('')
while i == 0:
    print('--- Menú de opciones ---')
    print('1. Mostrar detalles del pedido')
    print('2. Agregar Azúcar')
    print('3. Modificar Leche')
    print('4. Agrandar')
    print('5. Confirmar')
    opcion = int(input('Ingrese la opción deseada: '))
    print('')
    if opcion == 1:
        print('--- Mostrar detalles del pedido ---')
        print(nombre_cliente)
        print(nit_cliente)
        print('Licuado de fresa')
        print('Tamaño:', tamanio)
        print('Precio: ', precio)
        print('')
    elif opcion == 2:
        j = 0
        if azucar < 2:
            print('--- Agregar Azúcar ---')
            while j == 0:     
                azucar = azucar + 0.50
                precio = precio +  azucar
                print('Azúcar agregada')
                print('¿Desea agregar más azúcar? (s/n): ')
                opciona = input()
                print('')
                if opciona == "s":
                    if azucar == 2:
                        print('No se puede agregar más azúcar')
                        break
                    print('')
                elif opciona == "n":
                    break
                print('')
        else:
            print('No se puede agregar más azúcar')
            print('')
        
    elif opcion == 3:
        print('--- Modificar Leche ---')
        print('1. Sin leche')
        print('2. Leche deslactosada')
        print('3. Leche entera')
        print('4. Leche de soya')
        opcion_leche = int(input('Ingrese la opción deseada: '))
        if opcion_leche == 1:
            print('--- Sin leche ---')
            precio = precio - 2.00   
            print('')
            leche = 'Sin leche'
        elif opcion_leche == 2:
            print('--- Leche deslactosada ---')
            leche = 'Deslactosada'
            print('')
        elif opcion_leche == 3:
            print('--- Leche entera ---')
            leche = 'Entera'
            print('')
        elif opcion_leche == 4:
            print('--- Leche de soya ---')
            precio = precio + 3.00
            leche = 'Soya'
            print('')
        
    elif opcion == 4:
        print('--- Agrandar ---')
        if agrandado == False:
            porcentaje = precio * 0.05
            precio = precio + porcentaje
            agrandado = True
            tamanio = 'Grande'
            print('')
        else:
            print('Ya se ha agrandado')
            print('')
            
    elif opcion == 5:
        print('Nombre:', nombre_cliente)
        print('NIT', nit_cliente)
        print('Precio:', precio)
        print('Agrandado: ', agrandado)
        print('Tipo de leche: ', leche)
        print('Cucharadas de azúcar: ', azucar)
        print('Gracias por la compra')
        i = 1