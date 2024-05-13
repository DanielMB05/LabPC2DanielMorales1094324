print("Semana 10 Ejercicio 2")
def obtener_signo_zodiacal(dia, mes, año):
  
  signos_zodiacales = {
    "Aries": ((3, 21), (4, 19)),
    "Tauro": ((4, 20), (5, 20)),
    "Géminis": ((5, 21), (6, 20)),
    "Cáncer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Escorpión": ((10, 23), (11, 21)),
    "Sagitario": ((11, 22), (12, 21)),
    "Capricornio": ((12, 22), (1, 19)),
    "Acuario": ((1, 20), (2, 18)),
    "Piscis": ((2, 19), (3, 20)),
  }

  for signo, rango_fechas in signos_zodiacales.items():
    fecha_inicio, fecha_fin = rango_fechas
    if (mes == fecha_inicio[0] and dia >= fecha_inicio[1]) or \
       (mes == fecha_fin[0] and dia <= fecha_fin[1]):
      return signo

  return "Fecha no válida"


dia = int(input("Introduzca el día de su nacimiento: "))
mes = int(input("Introduzca el mes de su nacimiento: "))
año = int(input("Introduzca el año de su nacimiento: "))


signo_zodiacal = obtener_signo_zodiacal(dia, mes, año)


print(f"Su signo zodiacal es: {signo_zodiacal}")