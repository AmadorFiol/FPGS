Algoritmo numeroMayor
	Escribir "Dime un numero";
	Leer x;
	Escribir "Dime otro numero";
	Leer i;
	Escribir "Dime otro numero mas";
	Leer z;
	Escribir "X es ",x,", Y es ", i," y Z es ",z;
	Si x>i Entonces
		Si x>z Entonces
			Escribir "X es mayor que Y y Z";
		SiNo
			Escribir "Z es mayor que X e Y";
		FinSi
	SiNo
		Si i>z Entonces
			Escribir "Y es mayor que X y Z";
		SiNo
			Escribir "Z es mayor que X e Y";
		FinSi
	Fin Si
	
FinAlgoritmo
