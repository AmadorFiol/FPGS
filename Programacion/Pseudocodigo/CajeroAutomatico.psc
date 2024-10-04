Algoritmo CajeroAutomatico
	salir<-Falso
	saldo<-1000
	Mientras salir=Falso Hacer
		Escribir "Saldo: ",saldo
		Escribir "Que deseas hacer?"
		Escribir "1. Meter saldo"
		Escribir "2. Sacar saldo"
		Escribir "3. Salir"
		Leer accion
		Segun accion Hacer
			"1":
				Escribir "Cuanto saldo quieres añadir?"
				Leer x
				saldo<-saldo+x
				Limpiar Pantalla
			"2":
				Escribir "Cuanto saldo quieres sacar?"
				Leer x
				Si x>saldo Entonces
					Escribir "Saldo insuficiente para realizar la accion"
					Esperar 1 Segundos
					Escribir "Se ha cancelado la accion"
					Esperar 1 segundos
				SiNo
					saldo<-saldo-x
				FinSi
				Limpiar Pantalla
			"3":
				salir<-Verdadero
			De Otro Modo:
				Escribir "Ponga el numero de una de las opciones mostradas"
				Esperar 1 Segundos
				Limpiar Pantalla
		Fin Segun
	Fin Mientras
	
FinAlgoritmo
