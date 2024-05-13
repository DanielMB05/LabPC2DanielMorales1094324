

def case ():
    return 2*2
def case2 ():
    return 2-1
def case3 ():
    return 2+3
def default_case ():
    return "Opción no valida"
def switch_case(argument):
    switcher = {
        1:case,
        2:case2,
        3:case3
    }

    func = switcher.get (argument, default_case)
    return func()

opcion = 4

print(switch_case(opcion))
