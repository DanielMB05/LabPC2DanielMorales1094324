# Lista global para almacenar los cursos y los alumnos
cursos = []
alumnos = []
notas = []

# Función para crear un curso
def crear_curso(id_curso, nombre, horario, salon, catedratico):
    # Verificar si el curso ya existe
    for curso in cursos:
        if curso['id'] == id_curso:
            print("Error: Ya existe un curso con este ID.")
            return
    # Crear y agregar el curso
    curso = {
        'id': id_curso,
        'nombre': nombre,
        'horario': horario,
        'salon': salon,
        'catedratico': catedratico
    }
    cursos.append(curso)
    print("Curso creado exitosamente.")

# Función para listar los cursos
def listar_cursos():
    if not cursos:
        print("No hay cursos disponibles.")
        return
    for i, curso in enumerate(cursos, start=1):
        print(f"{i}. ID: {curso['id']}, Nombre: {curso['nombre']}, Horario: {curso['horario']}, Salón: {curso['salon']}, Catedrático: {curso['catedratico']}")

# Función para editar un curso
def editar_curso(id_curso, nombre=None, horario=None, salon=None, catedratico=None):
    for curso in cursos:
        if curso['id'] == id_curso:
            if nombre:
                curso['nombre'] = nombre
            if horario:
                curso['horario'] = horario
            if salon:
                curso['salon'] = salon
            if catedratico:
                curso['catedratico'] = catedratico
            print("Curso actualizado exitosamente.")
            return
    print("Error: No se encontró un curso con ese ID.")

# Función para crear un alumno
def crear_alumno(carne, nombre, fecha_nacimiento):
    # Verificar si el alumno ya existe
    for alumno in alumnos:
        if alumno['carne'] == carne:
            print("Error: Ya existe un alumno con este Carné.")
            return
    # Crear y agregar el alumno
    alumno = {
        'carne': carne,
        'nombre': nombre,
        'fecha_nacimiento': fecha_nacimiento
    }
    alumnos.append(alumno)
    print("Alumno creado exitosamente.")

# Función para editar un alumno
def editar_alumno(carne, nombre=None, fecha_nacimiento=None):
    for alumno in alumnos:
        if alumno['carne'] == carne:
            if nombre:
                alumno['nombre'] = nombre
            if fecha_nacimiento:
                alumno['fecha_nacimiento'] = fecha_nacimiento
            print("Alumno actualizado exitosamente.")
            return
    print("Error: No se encontró un alumno con ese Carné.")

# Función para asignar una nota a un alumno en un curso
def asignar_nota(carne, id_curso, nota):
    # Verificar si el alumno y el curso existen
    alumno_existe = any(alumno['carne'] == carne for alumno in alumnos)
    curso_existe = any(curso['id'] == id_curso for curso in cursos)
    if not alumno_existe:
        print("Error: No se encontró un alumno con ese Carné.")
        return
    if not curso_existe:
        print("Error: No se encontró un curso con ese ID.")
        return
    # Asignar la nota
    nota_entry = {
        'carne': carne,
        'id_curso': id_curso,
        'nota': nota
    }
    notas.append(nota_entry)
    print("Nota asignada exitosamente.")

# Funciones para los reportes
def reporte_cursos_con_cantidad_estudiantes():
    if not cursos:
        print("No hay cursos disponibles.")
        return
    reporte = []
    for curso in cursos:
        cantidad_estudiantes = sum(1 for nota in notas if nota['id_curso'] == curso['id'])
        reporte.append((curso['nombre'], cantidad_estudiantes))
    reporte.sort(key=lambda x: x[1], reverse=True)
    for curso, cantidad in reporte:
        print(f"Curso: {curso}, Cantidad de estudiantes: {cantidad}")

def reporte_estudiantes_con_notas(id_curso):
    curso_existe = any(curso['id'] == id_curso for curso in cursos)
    if not curso_existe:
        print("Error: No se encontró un curso con ese ID.")
        return
    estudiantes = [nota for nota in notas if nota['id_curso'] == id_curso]
    if not estudiantes:
        print("No hay estudiantes en este curso.")
        return
    for nota in estudiantes:
        alumno = next((alumno for alumno in alumnos if alumno['carne'] == nota['carne']), None)
        if alumno:
            print(f"Alumno: {alumno['nombre']}, Carné: {alumno['carne']}, Nota: {nota['nota']}")

def reporte_notas_por_estudiante(carne):
    alumno_existe = any(alumno['carne'] == carne for alumno in alumnos)
    if not alumno_existe:
        print("Error: No se encontró un alumno con ese Carné.")
        return
    estudiante_notas = [nota for nota in notas if nota['carne'] == carne]
    if not estudiante_notas:
        print("No hay notas para este estudiante.")
        return
    for nota in estudiante_notas:
        curso = next((curso for curso in cursos if curso['id'] == nota['id_curso']), None)
        if curso:
            print(f"Curso: {curso['nombre']}, Nota: {nota['nota']}")

def reporte_nota_media_por_curso():
    if not cursos:
        print("No hay cursos disponibles.")
        return
    for curso in cursos:
        notas_curso = [nota['nota'] for nota in notas if nota['id_curso'] == curso['id']]
        if notas_curso:
            nota_media = sum(notas_curso) / len(notas_curso)
            print(f"Curso: {curso['nombre']}, Nota media: {nota_media:.2f}")
        else:
            print(f"Curso: {curso['nombre']}, No hay notas asignadas.")

def reporte_mejor_estudiante():
    if not alumnos or not notas:
        print("No hay estudiantes o notas disponibles.")
        return
    promedio_notas = {}
    for alumno in alumnos:
        notas_alumno = [nota['nota'] for nota in notas if nota['carne'] == alumno['carne']]
        if notas_alumno:
            promedio_notas[alumno['carne']] = sum(notas_alumno) / len(notas_alumno)
    if not promedio_notas:
        print("No hay notas asignadas a los estudiantes.")
        return
    mejor_estudiante_carne = max(promedio_notas, key=promedio_notas.get)
    mejor_estudiante = next((alumno for alumno in alumnos if alumno['carne'] == mejor_estudiante_carne), None)
    if mejor_estudiante:
        print(f"Mejor estudiante: {mejor_estudiante['nombre']}, Carné: {mejor_estudiante['carne']}, Promedio: {promedio_notas[mejor_estudiante_carne]:.2f}")

# Bucle principal del menú
loop = True
while loop:
    print("\nMenú:")
    print("1. Crear curso")
    print("2. Listar cursos")
    print("3. Editar curso")
    print("4. Crear alumno")
    print("5. Editar alumno")
    print("6. Asignar nota")
    print("7. Reportes")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        id_curso = input("Ingrese el ID del curso: ")
        nombre = input("Ingrese el nombre del curso: ")
        horario = input("Ingrese el horario del curso: ")
        salon = input("Ingrese el salón del curso: ")
        catedratico = input("Ingrese el catedrático del curso: ")
        crear_curso(id_curso, nombre, horario, salon, catedratico)
        
    elif opcion == "2":
        listar_cursos()
        
    elif opcion == "3":
        id_curso = input("Ingrese el ID del curso a editar: ")
        nombre = input("Ingrese el nuevo nombre del curso (deje en blanco para no cambiar): ")
        horario = input("Ingrese el nuevo horario del curso (deje en blanco para no cambiar): ")
        salon = input("Ingrese el nuevo salón del curso (deje en blanco para no cambiar): ")
        catedratico = input("Ingrese el nuevo catedrático del curso (deje en blanco para no cambiar): ")
        editar_curso(id_curso, nombre if nombre else None, horario if horario else None, salon if salon else None, catedratico if catedratico else None)
        
    elif opcion == "4":
        carne = input("Ingrese el Carné del alumno: ")
        nombre = input("Ingrese el nombre del alumno: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (YYYY-MM-DD): ")
        crear_alumno(carne, nombre, fecha_nacimiento)
        
    elif opcion == "5":
        carne = input("Ingrese el Carné del alumno a editar: ")
        nombre = input("Ingrese el nuevo nombre del alumno (deje en blanco para no cambiar): ")
        fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del alumno (deje en blanco para no cambiar): ")
        editar_alumno(carne, nombre if nombre else None, fecha_nacimiento if fecha_nacimiento else None)
        
    elif opcion == "6":
        carne = input("Ingrese el Carné del alumno: ")
        id_curso = input("Ingrese el ID del curso: ")
        nota = float(input("Ingrese la nota del alumno: "))
        asignar_nota(carne, id_curso, nota)
        
    elif opcion == "7":
        print("\nReportes:")
        print("1. Listado de cursos con cantidad de estudiantes")
        print("2. Listar estudiantes de un curso con sus notas")
        print("3. Listar notas de un estudiante")
        print("4. Nota media por curso")
        print("5. Estudiante con mejor desempeño")
        reporte_opcion = input("Seleccione un reporte: ")
        
        if reporte_opcion == "1":
            reporte_cursos_con_cantidad_estudiantes()
        elif reporte_opcion == "2":
            id_curso = input("Ingrese el ID del curso: ")
            reporte_estudiantes_con_notas(id_curso)
        elif reporte_opcion == "3":
            carne = input("Ingrese el Carné del estudiante: ")
            reporte_notas_por_estudiante(carne)
        elif reporte_opcion == "4":
            reporte_nota_media_por_curso()
        elif reporte_opcion == "5":
            reporte_mejor_estudiante()
        else:
            print("Opción de reporte inválida.")
            
    elif opcion == "8":
        loop = False
        
    else:
        print("Opción inválida.")
        