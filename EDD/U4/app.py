def calcular_promedio(notas):
    suma=0
    for nota in notas:
        suma+=nota
    promedio=suma/nota
    return promedio

def obtener_notas():
    notas=[]
    for i in range(3):
        nota=input(f"Introduce la nota del estudiante {i+1}: ")
        notas.append(int(nota))
    return notas

notas=obtener_notas()
promedio=calcular_promedio(notas)
print(f"El promedio de notas es {promedio}")