Algoritmo PositivoONegativo
	Escribir "Dime un numero";
	Leer x;
	xEs0<-Verdadero;
	
	Mientras xEs0=Verdadero
		Si x=0 Entonces
			Escribir "El numero es igual a 0";
			Escribir "Dime otro numero que no sea 0";
			Leer x;
		SiNo	
			Si x<0 Entonces
				Escribir "El numero es negativo";
			SiNo
				Escribir "El numero es positivo";
			FinSi
			xEs0<-Falso;
		FinSi
	FinMientras

FinAlgoritmo
