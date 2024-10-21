Algoritmo calculadora
	salir<-Falso
	Mientras salir=Falso
		Escribir "Que vas a hacer?"
		Escribir "1. Suma"
		Escribir "2. Resta"
		Escribir "3. Multiplicacion"
		Escribir "4. Division"
		Escribir "5. Salir"
		Leer input
		
		Segun input
			"1":
				Escribir "Cual sera el primer numero?"
				Leer x
				Escribir "Cual sera el segundo numero?"
				Leer i
				z<-x+i
				Escribir "El resultado de la suma es:",z
			"2":
				Escribir "Cual sera el primer numero?"
				Leer x
				Escribir "Cual sera el segundo numero?"
				Leer i
				z<-x-i
				Escribir "El resultado de la resta es: ",z
			"3":
				Escribir "Cual sera el primer numero?"
				Leer x
				Escribir "Cual sera el segundo numero?"
				Leer i
				z<-x*i
				Escribir "El resultado de la multiplicacion es:", z
			"4":
				Escribir "Cual sera el primer numero?"
				Leer x
				Escribir "Cual sera el segundo numero?"
				Leer i
				z<-x/i
				Escribir "El resultado de la division es:", z
			"5":
				salir<-Verdadero
			De Otro Modo:
				Escribir "Escriba una de las opciones disponibles"
		FinSegun
		Esperar 2 Segundos
		Limpiar Pantalla
	FinMientras
FinAlgoritmo
