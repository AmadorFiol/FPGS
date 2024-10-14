Algoritmo ExamenUD1
	Escribir "Ingrese la cantidad de numeros"
	Leer nums
	Dimension lista[nums]
	Para i<-1 hasta nums Con Paso 1 Hacer
		Escribir "ingrese el num", i
		Leer lista[i]
	FinPara
	Escribir "Media Aritmetica:"
	sum=0
	Para i<-1 hasta nums Con Paso 1 Hacer
		sum=sum+lista[i]
	FinPara
	Escribir "La media aritmetica es: " sum/nums
	Escribir "Suma Dobles:"
	sum=0
	Para i<-1 hasta nums Con Paso 1 Hacer
		sum=sum+(lista[i]*2)
		
	FinPara
	Escribir "La suma del doble de cada numero es:", sum
	Escribir "Multiplicacion de los pares:"
	mult=1
	Para i<-1 hasta nums Con Paso 1 Hacer
		Si (i%2)=0
			mult=mult*lista[i]
		FinSi
	FinPara
	Escribir "La multiplicacion de los números pares que se encuentrarn en posicion par es:" mult
FinAlgoritmo
