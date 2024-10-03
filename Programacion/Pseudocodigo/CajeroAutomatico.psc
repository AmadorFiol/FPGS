Algoritmo CajeroAutomatico
	salir<-Falso
	saldo<-1000
	Mientras salir=Falso Hacer
		Escribir "Que deseas hacer?"
		Escribir "1. Meter saldo"
		Escribir "2. Sacar saldo"
		Escribir "3. Salir"
		Leer accion
		Segun accion Hacer
			1:
				Escribir "Cuanto saldo quieres añadir"
				Leer x
				x<-(x)//Aqui me quede
				saldo<-saldo+x
			2:
				secuencia_de_acciones_2
			3:
				salir<-Verdadero
			De Otro Modo:
				secuencia_de_acciones_dom
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
