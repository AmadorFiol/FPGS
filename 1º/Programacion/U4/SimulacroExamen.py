class Persona:
    def __init__(self,nombre,edad,correo):
        self.nombre=nombre
        self.edad=edad
        self.correo=correo

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_correo(self):
        return self.correo
    
    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_edad(self,edad):
        self.edad=edad
    
    def set_correo(self,correo):
        self.correo=correo

    def mostrar_info(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, edad, correo, matricula):
        super().__init__(nombre, edad, correo)
        self.matricula=matricula
        self.cursos_inscritos=[]

    def get_matricula(self):
        return self.matricula
    
    def get_cursos_inscritos(self):
        return self.cursos_inscritos
    
    def set_matricula(self,matricula):
        self.matricula=matricula

    def set_cursos_inscritos(self,curso):
        self.cursos_inscritos.append(curso)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo}\nMatricula: {self.matricula}")
        if len(self.cursos_inscritos)==0:
            print("Cursos Inscritos: Ninguno")
        else:
            print("Cursos Inscritos:",end=" ")
            for curso in self.cursos_inscritos:
                if curso != self.cursos_inscritos[-1]:
                    print(curso.nombre,end=", ")
                else:
                    print(curso.nombre)


class Profesor(Persona):
    def __init__(self, nombre, edad, correo):
        super().__init__(nombre, edad, correo)
        self.asignaturas=[]

    def get_asignaturas(self):
        return self.asignaturas

    def set_asignatura(self,asignatura):
        self.asignaturas.append(asignatura)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo}")
        if len(self.asignaturas)==0:
            print("Asignaturas: Ninguno")
        else:
            print("Asignaturas:",end=" ")
            for asignatura in self.asignaturas:
                if asignatura != self.asignaturas[-1]:
                    print(asignatura.nombre,end=", ")
                else:
                    print(asignatura.nombre)
    
class Curso:
    def __init__(self,nombre,codigo,profeAsignado):
        self.nombre=nombre
        self.codigo=codigo
        self.profeAsignado=profeAsignado
        self.estudiantes=[]

    def inscribir_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
        estudiante.set_cursos_inscritos(self)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nCodigo: {self.codigo}\nProfesor Asignado: {self.profeAsignado.nombre}")
        if len(self.estudiantes)==0:
            print("Estudiantes: Ninguno")
        else:
            print("Estiduantes:",end=" ")
            for estudiante in self.estudiantes:
                if estudiante != self.estudiantes[-1]:
                    print(estudiante.nombre,end=", ")
                else:
                    print(estudiante.nombre)

class SistemaGestionCursos():
    def __init__(self):
        self.estudiantes=[]
        self.profesores=[]
        self.cursos=[]
    
    def set_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)
    
    def set_profesor(self,profesor):
        self.profesores.append(profesor)

    def set_curso(self,curso):
        self.cursos.append(curso)
        curso.profeAsignado.set_asignatura(curso)

    def show_estudiantes(self):
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante.nombre)

    def show_profesores(self):
        print("Profesores:")
        for profesor in self.profesores:
            print(profesor.nombre)

    def show_cursos(self):
        print("Cursos")
        for curso in self.cursos:
            print(curso.nombre)

#-----Inizializacion variables-----#
sgc=SistemaGestionCursos()

p1=Profesor("Carlos",35,"carlos@profe.sjo.com")
sgc.set_profesor(p1)

p2=Profesor("Santi",35,"santi@profe.sjo.com")
sgc.set_profesor(p2)


e1=Estudiante("Amador",19,"amador@alumno.sjo.com",100)
sgc.set_estudiante(e1)

e2=Estudiante("Adrian",21,"adrian@alumno.sjo.com",101)
sgc.set_estudiante(e2)

e3=Estudiante("Isaac",25,"isaac@alumno.sjo.com",102)
sgc.set_estudiante(e3)

c1=Curso("Programacion",1,p1)
sgc.set_curso(c1)

c2=Curso("Base de Datos",2,p2)
sgc.set_curso(c2)

#-----Main-----#
print("#-----Curso 1-----#")
c1.inscribir_estudiante(e1)
c1.inscribir_estudiante(e2)
c1.mostrar_info()
print("\n#-----Curso 2-----#")
c2.inscribir_estudiante(e1)
c2.inscribir_estudiante(e3)
c2.mostrar_info()
print("\n#-----Estudiante 1-----#")
e1.mostrar_info()
print("\n#-----Estudiante 2-----#")
e2.mostrar_info()
print("\n#-----Estudiante 3-----#")
e3.mostrar_info()
print("\n#-----Profesor 1-----#")
p1.mostrar_info()
print("\n#-----Profesor 2-----#")
p2.mostrar_info()