def display_menu():
    """Displays the restaurant menu."""
    print("**Welcome to The Syringe Restaurant**")
    print("-" * 30)
    print("1. Hamburguesa clásica (Classic Hamburger) - $15.00")
    print("2. Pizza pepperoni (Pepperoni Pizza) - $20.00")
    print("3. Ensalada César (Caesar Salad) - $12.00")
    print("4. Helado de chocolate (Chocolate Ice Cream) - $8.00")
    print("5. Bebida (Refresco o agua) (Drink (Soda or Water)) - $2.00")
    print("6. Salir (Exit)")
    print("-" * 30)

def take_order():
    """Takes the customer's order."""
    while True:
        try:
            option = int(input("Ingrese el número de la opción que desea: (Enter the number of the option you want): "))
            if 1 <= option <= 6:
                break
            else:
                print("Opción no válida. Intente de nuevo. (Invalid option. Try again.)")
        except ValueError:
            print("No ingresó un número. Intente de nuevo. (You did not enter a number. Try again.)")

    quantity = int(input("¿Cuántas unidades desea de la opción elegida?: (How many units do you want of the chosen option?): "))
    return option, quantity

def calculate_total_price(option, quantity):
    """Calculates the total price of the order."""
    if option == 1:
        price_per_unit = 15.00
    elif option == 2:
        price_per_unit = 20.00
    elif option == 3:
        price_per_unit = 12.00
    elif option == 4:
        price_per_unit = 8.00
    elif option == 5:
        price_per_unit = 2.00
    else:
        price_per_unit = 0.00

    total_price = price_per_unit * quantity
    return total_price

def process_order(option, quantity, total_price):
    """Processes the order and displays the order details."""
    print(f"Su pedido es: {quantity} unidad(es) de la opción {option} (Your order is: {quantity} unit(s) of option {option})")
    print(f"El precio total es: ${total_price:.2f} (Total price is: ${total_price:.2f})")

def main():
    """Runs the main program loop."""
    display_menu()

    while True:
        option, quantity = take_order()

        if option == 6:
            print("¡Gracias por su visita! (Thank you for your visit!)")
            break

        total_price = calculate_total_price(option, quantity)
        process_order(option, quantity, total_price)

        another_order = input("¿Desea agregar algo más a su pedido? (sí/no) (Do you want to add anything else to your order? (yes/no)): ").lower()
        if another_order != "sí":
            break

if __name__ == "__main__":
    main()
