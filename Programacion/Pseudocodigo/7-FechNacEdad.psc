Algoritmo FechNacEdad
	Escribir "En que dia naciste?"
	Leer dia
	Escribir "De que mes?"
	leer mes
	Escribir "Y de que a�o?"
	Leer a�o
	Escribir "Que dia es hoy?"
	Leer diaActual
	Escribir "De que mes?"
	Leer mesActual
	Escribir "Y de que a�o?"
	Leer a�oActual
	edad<-a�oActual-a�o
	Si(mes>mesActual) o (mes=mesActual y dia>diaActual) Entonces
		edad<-edad-1
		
	FinSi
	Escribir "Tienes ",edad," a�os"
FinAlgoritmo
