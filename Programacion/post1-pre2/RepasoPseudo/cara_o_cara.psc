Algoritmo cara_o_cara
	J1puntos<-0
	J2puntos<-0
	Mientras J1puntos<5 y J2puntos<5 Hacer
		Escribir "Marcador ",J1puntos,":",J2puntos
		Escribir ""
		Escribir "Turno J1"
		Segun Azar(2) Hacer
			0:
				Escribir "Ha salido cruz"
			1:
				Escribir "Ha salido cara!"
				J1puntos<-J1puntos+1
		FinSegun
		Esperar 2 Segundos
		Limpiar Pantalla
		Escribir "Marcador ",J1puntos,":",J2puntos
		Escribir ""
		Escribir "Turno J2"
		Segun Azar(2) Hacer
			0:
				Escribir "Ha salido cruz"
			1:
				Escribir "Ha salido cara!"
				J2puntos<-J2puntos+1
		FinSegun
		Esperar 2 Segundos
		Limpiar Pantalla
	FinMientras
	Escribir "Marcador ",J1puntos,":",J2puntos
	Si J1puntos=5 y J2puntos<>5 Entonces
		Escribir "Ha ganado el J1"
	SiNo
		Si J2puntos=5 y J1puntos<>5 Entonces
			Escribir "Ha ganado el J2"
		SiNo
			Escribir "HA SIDO UN EMPATE"
		FinSi
	FinSi
FinAlgoritmo
