# curso.py
class Curso:
    def __init__(self, id, nombre, horario, salon, catedratico):
        self.id = id
        self.nombre = nombre
        self.horario = horario
        self.salon = salon
        self.catedratico = catedratico

    def __str__(self):
        return f"Curso {self.nombre} - {self.horario} - {self.salon} - {self.catedratico}"

class CursoController:
    def __init__(self):
        self.cursos = []

    def crear_curso(self, id, nombre, horario, salon, catedratico):
        if self.existe_curso(id):
            print("Curso ya existe")
            return
        curso = Curso(id, nombre, horario, salon, catedratico)
        self.cursos.append(curso)
        print("Curso creado exitosamente")

    def editar_curso(self, id, nombre, horario, salon, catedratico):
        for curso in self.cursos:
            if curso.id == id:
                curso.nombre = nombre
                curso.horario = horario
                curso.salon = salon
                curso.catedratico = catedratico
                print("Curso editado exitosamente")
                return
        print("Curso no encontrado")

    def existe_curso(self, id):
        for curso in self.cursos:
            if curso.id == id:
                return True
        return False

    def listar_cursos(self):
        for curso in self.cursos:
            print(curso)

# alumno.py
class Alumno:
    def __init__(self, carnet, nombre, fecha_nacimiento):
        self.carnet = carnet
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Alumno {self.nombre} - {self.carnet} - {self.fecha_nacimiento}"

class AlumnoController:
    def __init__(self):
        self.alumnos = []

    def crear_alumno(self, carnet, nombre, fecha_nacimiento):
        alumno = Alumno(carnet, nombre, fecha_nacimiento)
        self.alumnos.append(alumno)
        print("Alumno creado exitosamente")

    def editar_alumno(self, carnet, nombre, fecha_nacimiento):
        for alumno in self.alumnos:
            if alumno.carnet == carnet:
                alumno.nombre = nombre
                alumno.fecha_nacimiento = fecha_nacimiento
                print("Alumno editado exitosamente")
                return
        print("Alumno no encontrado")

    def listar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno)

# calificacion.py
class Calificacion:
    def __init__(self, curso, alumno, nota):
        self.curso = curso
        self.alumno = alumno
        self.nota = nota

class CalificacionController:
    def __init__(self):
        self.calificaciones = []

    def asignar_nota(self, curso, alumno, nota):
        calificacion = Calificacion(curso, alumno, nota)
        self.calificaciones.append(calificacion)
        print("Nota asignada exitosamente")

    def listar_calificaciones(self):
        for calificacion in self.calificaciones:
            print(f"Curso {calificacion.curso.nombre} - Alumno {calificacion.alumno.nombre} - Nota {calificacion.nota}")

# reporte.py
class ReporteController:
    def __init__(self, curso_controller, alumno_controller, calificacion_controller):
        self.curso_controller = curso_controller
        self.alumno_controller = alumno_controller
        self.calificacion_controller = calificacion_controller

    def reporte_cursos(self):
        cursos = self.curso_controller.cursos
        cursos.sort(key=lambda x: len([calificacion for calificacion in self.calificacion_controller.calificaciones if calificacion.curso == x]), reverse=True)
        for curso in cursos:
            print(f"Curso {curso.nombre} - {len([calificacion for calificacion in self.calificacion_controller.calificaciones if calificacion.curso == curso])} estudiantes")

    def reporte_alumnos_curso(self, curso_id):
        curso = next((curso for curso in self.curso_controller.cursos if curso.id == curso_id), None)
        if curso is None:
            print("Curso no encontrado")
            return
        alumnos = [calificacion.alumno for calificacion in self.calificacion_controller.calificaciones if calificacion.curso == curso]
        for alumno in alumnos:
            print(f"Alumno {alumno.nombre} - Nota {next((calificacion.nota for calificacion in self.calificacion_controller.calificaciones if calificacion.alumno == alumno and calificacion.curso == curso))}")