'''
Escribir un programa que:
Recorra el diccionario y calcule el promedio de calificaciones de cada estudiante.
Calcule el alumno que ha sacado la nota más alta
Calcule el promedio global de todas las calificaciones
'''
notaMax=["nombre","asignatura",0]
sumMedia=0
calificaciones = {
    "Juan Pérez": {
        "Matemáticas": 7.5,
        "Física": 8.0,
        "Química": 6.0,
        "Historia": 9.0
    },
    "Ana López": {
        "Matemáticas": 4.0,
        "Física": 5.5,
        "Química": 6.0,
        "Historia": 8.5
    },
    "Carlos Ruiz": {
        "Matemáticas": 9.0,
        "Física": 8.0,
        "Química": 7.5,
        "Historia": 6.0
    },
    "Luisa Gómez": {
        "Matemáticas": 3.5,
        "Física": 4.0,
        "Química": 5.0,
        "Historia": 6.5
    }
}

for estudiante in calificaciones:
    print(estudiante)
    sumNota=0
    for asignatura,nota in calificaciones[estudiante].items():
        sumNota=sumNota+nota
        if nota>notaMax[2]:
            notaMax=[estudiante,asignatura,nota]
    mediaNota=sumNota/len(calificaciones[estudiante])
    sumMedia=sumMedia+mediaNota
    print(mediaNota)
print("\nEl estudiante con la mayor nota a sido",notaMax[0],"con un",notaMax[2],"en",notaMax[1])
print("La media global es", sumMedia/len(calificaciones))