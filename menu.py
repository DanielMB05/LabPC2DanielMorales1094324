def main():
    # Opciones del Menú
    print("Bienvenido a nuestro restaurante!")
    print("Menú:")
    print("1. Desayuno")
    print("2. Almuerzo")
    print("3. Cena")

    # Selección del usuario
    selection = int(input("Ingrese su selección: "))

    # Proceso
    if selection == 1:
        breakfast_selection = int(input("Elija una opción de desayuno:\n"
                                       "1. Bowl de frutas con yogurt ($30.00)\n"))
        if breakfast_selection == 1:
            total = 30.00
        else:
            print("Opción no válida")
            return

    elif selection == 2:
        lunch_selection = int(input("Elija una opción de almuerzo:\n"
                                    "1. Costillas a la barbacoa con 2 acompañamientos y jugo natural ($35.00)\n"))
        if lunch_selection == 1:
            total = 35.00
        else:
            print("Opción no válida")
            return

    elif selection == 3:
        dinner_selection = int(input("Elija una opción de cena:\n"
                                     "1. Huevos estrellados, frijoles, plátanos y crema con café ($30.00)\n"))
        if dinner_selection == 1:
            total = 30.00
        else:
            print("Opción no válida")
            return

    else:
        print("Opción no válida")
        return

    # Preguntar si el usuario desea agregar algo más a su orden
    add_more = input("¿Desea agregar algo más a su pedido? (Sí/No): ").lower()

    if add_more == "sí":
        # Articulo adicional
        int(input("seleccione una opción"))
         if selection == 1:
        breakfast_selection = int(input("Elija una opción de desayuno:\n"
                                       "1. Bowl de frutas con yogurt ($30.00)\n"))
        if breakfast_selection == 1:
            total = 30.00
        else:
            print("Opción no válida")
            return

    elif selection == 2:
        lunch_selection = int(input("Elija una opción de almuerzo:\n"
                                    "1. Costillas a la barbacoa con 2 acompañamientos y jugo natural ($35.00)\n"))
        if lunch_selection == 1:
            total = 35.00
        else:
            print("Opción no válida")
            return

    elif selection == 3:
        dinner_selection = int(input("Elija una opción de cena:\n"
                                     "1. Huevos estrellados, frijoles, plátanos y crema con café ($30.00)\n"))
        if dinner_selection == 1:
            total = 30.00
        else:
            print("Opción no válida")
            return

    else:
        print("Opción no válida")
        return
        add_more = input("¿Desea agregar algo más a su pedido? (Sí/No): ").lower()


    # Total
    print("El total de su pedido es:", total)

    # Confirmación de la orden
    confirm_order = input("¿Desea confirmar su pedido? (Sí/No): ").lower()

    if confirm_order == "sí":
        print("Su pedido ha sido confirmado. ¡Gracias por su compra!")
    else:
        print("Su pedido ha sido cancelado.")


if __name__ == "__main__":
    main()