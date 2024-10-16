persona1={
    "Nombre":"Amador",
    "Apellido1":"Fiol",
    "Apellido2":"Borel",
    "Edad":18
}
persona2={
    "Nombre":"Aina",
    "Apellido1":"Cruz",
    "apellido2":"Sanchez",
    "edad":19
}
persona3={
    "Nombre":"Juan",
    "Apellido1":"Pulido",
    "Apellido2":"Colmenero",
    "Edad":20
}
persona4={
    "Nombre":"Sandra",
    "Apellido1":"Pulido",
    "Apellido2":"Colmenero",
    "Edad":22
}

personas={
    "12345678A":persona1,
    "12345678B":persona2,
    "12345678C":persona3,
    "12345678D":persona4
}
padre=input("Cual es el DNI del padre? ")
madre=input("Cual es el DNI de la madre? ")

nombre=input("Cual es el nombre del hijo/a? ")

print("El nombre completo del nacido es: ",nombre,personas[padre]["Apellido1"],personas[madre]["Apellido1"])

'''
Dinamismo mejorado

Array con DNI's
input usuario
Bucle en la que:
    Si no existe una persona con ese DNI pedir datos de dicha persona
        Si existe indicar la existencia de esa persona

'''