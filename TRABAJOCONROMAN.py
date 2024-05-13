def print_multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

def find_max_number():
    numbers = [float(input("Ingrese un número: ")) for _ in range(5)]
    max_number = max(numbers)
    print("El número máximo es:", max_number)

def exit_program():
    print("¡Adiós!")
    quit()

menu_options = {
    1: find_max_number,
    2: lambda: [print(f"Tabla de multiplicar para {i}:") or print_multiplication_table(i) for i in range(1, 11)],
    3: exit_program
}

print("¡Bienvenido al menú!")
while True:
    print("\n1. Ingrese 5 números y encuentre el máximo")
    print("2. Imprima tablas de multiplicar del 1 al 10")
    print("3. Salir")
    choice = int(input("Ingrese su opción: "))
    action = menu_options.get(choice)
    if action:
        action()
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")