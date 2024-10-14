pelicula1={"titulo":"Spider-man","año":2002,"director":"Stan Lee","genero":"Accion"}
pelicula2={"titulo":"Titanic","año":1997,"director":"James Cameron","genero":"Romance"}
pelicula3={"titulo":"Gru, Mi villano favorito","año":2010,"director":"Chris Renaud","genero":"Comedia"}

peliculas={
    1:pelicula1,
    2:pelicula2,
    3:pelicula3
}


for i in peliculas:
    print(i,".",peliculas[i]["titulo"])


id=int(input("Cual es el ID de la peli que deseas ver? "))
print(f"{peliculas[id]["titulo"]} fue publicada en el año {peliculas[id]["año"]} por el director {peliculas[id]["director"]}")