Algoritmo ExamenUD1
	Escribir "Act1"
	Escribir "Dime un numero"
	Leer num
	Si num<=0 Entonces
		Escribir "Este numero es negativo o es 0"
	SiNo
		cuadrado<-num^2
		Escribir "El cuadrado de ", num," es ",cuadrado
	FinSi
	
	Esperar 2 Segundos
	Limpiar Pantalla
	Escribir "Act2"
	Escribir "Dime un numero"
	Leer num
	factorial<-num
	Para i<-1 Hasta num-1 Con Paso 1 Hacer
		factorial<-factorial*i
	FinPara
	Escribir "El factorial de ", num," es ",factorial
	
	Esperar 2 Segundos
	Limpiar Pantalla
	Escribir "Act3"
	passCorrecta=Falso
	intentosRestantes<-3
	Mientras passCorrecta<>Verdadero Hacer
		Escribir "Dime la contraseña"
		Leer clave
		Si clave="sjo" Entonces
			Escribir "Contraseña correcta"
			passCorrecta<-Verdadero
		SiNo
			Si intentosRestantes>0 Entonces
				Escribir "Contraseña incorrecta, te quedan ",intentosRestantes," intentos restantes"
				intentosRestantes<-intentosRestantes-1
				Esperar 2 Segundos
				Limpiar Pantalla
			SiNo
				Escribir "Se te han acabado los intentos"
				passCorrecta<-Verdadero
			FinSi
		FinSi
	FinMientras
	
FinAlgoritmo
