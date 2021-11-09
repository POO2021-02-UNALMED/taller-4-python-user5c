

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None, grado="Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas or []
        self.listadoAlumnos = estudiantes or []
        Grupo.grado = grado

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        self.listadoAlumnos = lista + [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self) -> str:
        if self._grupo == "grupo ordinado":
            return "Grupo de estudiantes: grupo predeterminado"
        
        return "Grupo de estudiantes: " + self._grupo
