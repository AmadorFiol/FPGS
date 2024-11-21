'''
Se ha de usar la funcion zip()
Pedir por pantalla el nombre de varios alumnos y almacenarlos en una lista
Pedir por pantalla la nota que sacaron y guardarla en otra lista
Recorrer las lista y escribir por pantalla un mensaje como
"El alumno $nombre ha obtenido una calificacion de $nota"
'''
alumnoArray=[]
notaArray=[]
cantidad=int(input("Cuantos alumnos se van a presentar? "))
for i in range(0,cantidad):
    alumnoArray.append(input(f"Nombre del alumno {i+1}: "))
    notaArray.append(input("Que nota ha sacado? "))

for alumno,nota in zip(alumnoArray,notaArray):
    print("El alumno",alumno,"ha sacado un",nota)