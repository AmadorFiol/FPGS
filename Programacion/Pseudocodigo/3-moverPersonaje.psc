Algoritmo moverPersonaje
	Cerrar<-Falso
	Escribir "Hacia donde quieres moverte? (WASD o Q para finalizar)";
	Mientras Cerrar=Falso
		Leer movimiento;
		Segun movimiento Hacer
			"w" o "W":
				Escribir "Te has movido hacia arriba";
			"a" o "A":
				Escribir "Te has movido hacia la izquierda";
			"s" o "S":
				Escribir "Te has movido hacia abajo";
			"d" o "D":
				Escribir "Te has movido hacia la derecha";
			"q" o "Q":
				Cerrar<-Verdadero;
			De Otro Modo:
				Escribir "Esa no es una direccion adimitida";
		Fin Segun
	FinMientras
FinAlgoritmo
