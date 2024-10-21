Algoritmo marcador_futbol
	golLocal<-0
	golVisitante<-0
	Escribir "Cual es el equipo local?"
	Leer nombreLocal
	Escribir "Y el visitante?"
	Leer nombreVisitante
	
	Escribir "¡Que comience el partido!"
	Esperar 2 Segundos
	Limpiar Pantalla
	Mientras (golLocal<3) y (golVisitante<3) Hacer
		Escribir "Marcador: ",golLocal,":",golVisitante
		Escribir ""
		Escribir "GOOOOL, ¿pero de que equipo a sido?"
		Escribir "1. Equipo Local (",nombreLocal,")"
		Escribir "2. Equipo Visitante (", nombreVisitante ")"
		Leer golDe
		Segun golDe
			"1" o nombreLocal:
				golLocal<-golLocal+1
				Escribir "GOL DE ",nombreLocal
			"2" o nombreVisitante:
				golVisitante<-golVisitante+1
				Escribir "GOL DE ", nombreVisitante
			De Otro Modo:
				Escribir ""
		FinSegun
		Esperar 2 Segundos
		Limpiar Pantalla
	FinMientras
	Escribir "Marcador: ",golLocal,":",golVisitante
	Si golLocal=3 Entonces
		Escribir "HA GANADO ",nombreLocal
	SiNo
		Escribir "HA GANADO ",nombreVisitante
	FinSi
FinAlgoritmo
