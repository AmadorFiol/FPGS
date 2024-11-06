d1={'id':"a",'nombre':"Hombres G",'genero':"pop",'discos':11,'primer_disc':1997}
d2={'id':"b",'nombre':"Imagine Dragrons",'genero':"rock",'discos':7,'primer_disc':2001}
d3={'id':"c",'nombre':"Boy With Uke",'genero':"pop",'discos':5,'primer_disc':2005}
d4={'id':"d",'nombre':"Morat",'genero':"pop",'discos':8,'primer_disc':2000}
print("Vamos a añadir un artista a la lista, pero primero necesito algunos datos")
nombreIn=input("Dime el nombre del artista o grupo: ")
generoIn=input("Dime el genero musical que tiene en general sus canciones: ")
discosIn=input("Cuantos discos ha sacado? ")
primerIn=input("Cuando salió el primero? ")
d5={'id':"e",'nombre':nombreIn,'genero':generoIn,'discos':discosIn,'primer_disc':primerIn}
def mostrar_informacion(id):
    match(id):
        case "a":
            print("El artista/grupo", d1["nombre"]," del genero", d1['genero']," ha sacado un total de ",d1['discos']," discos siendo el primero en el año",d1['primer_disc'])
        case "b":
            print("El artista/grupo", d2["nombre"]," del genero", d2['genero']," ha sacado un total de ",d2['discos']," discos siendo el primero en el año",d2['primer_disc'])
        case "c":
            print("El artista/grupo", d3["nombre"]," del genero", d3['genero']," ha sacado un total de ",d3['discos']," discos siendo el primero en el año",d3['primer_disc'])
        case "d":
            print("El artista/grupo", d4["nombre"]," del genero", d4['genero']," ha sacado un total de ",d4['discos']," discos siendo el primero en el año",d4['primer_disc'])
        case "e":
            print("El artista/grupo", d5["nombre"]," del genero", d5['genero']," ha sacado un total de ",d5['discos']," discos siendo el primero en el año",d5['primer_disc'])
        case _:
            print("Ninguno de los artistas/grupos coincide con el id indicado")

salir=False
while(salir==False):
    print("")
    print("Escoge uno de los siguientes para ver la informacion o seleccione 'x' para salir")
    print("a. Hombres G")
    print("b. Imagine Dragons")
    print("c. Boy With Uke")
    print("d. Morat")
    print("e.",d5['nombre'])
    print("x. Salir")
    sel=input()
    sel=sel.lower()
    if(sel=="x"):
        salir=True
        print("Adios")
    else:
        print("")
        mostrar_informacion(sel)