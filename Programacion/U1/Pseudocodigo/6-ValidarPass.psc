Algoritmo ValidarPass
	passValid<-Falso
	Mientras passValid=Falso Hacer
		Escribir	"Escribe tu contraseña"
		Escribir "(Ha de tener 8 caracteres, 1 mayus y 1 num)"
		Leer password
		
		long8<-Falso
		hayMayus<-Falso
		hayNum<-Falso
		Si Longitud(password)<8 Entonces
			long8<-Falso
		SiNo
			long8<-Verdadero
		FinSi
		
		Para i<-1 Hasta Longitud(password) Hacer
			char<-Subcadena(password,i,i)
			//Compruebo si el valor ASCII de char esta entre la de "0" y "9"
			Si char >= "0" y char <= "9"
				hayNum<-Verdadero
			SiNo
				//En caso de que ya se haya cumplido la condicion
				//para verdadero evito que lo cambie
				Si hayNum<>Verdadero
					hayNum<-Falso
				FinSi
			FinSi
		FinPara
		
		Para i<-1 Hasta Longitud(password) Hacer
			char<-Subcadena(password,i,i)
			//Compruebo si el valor ASCII de char esta entre la de "A" y "Z"
			Si char >= "A" y char <= "Z"
				hayMayus<-Verdadero
			SiNo
				//En caso de que ya se haya cumplido la condicion
				//para verdadero evito que lo cambie
				Si hayMayus<>Verdadero
					hayMayus<-Falso
				FinSi
			FinSi
		FinPara
		
		Si NO(long8=Verdadero y hayNum=Verdadero y hayMayus=Verdadero)
			Escribir "Esta contraseña no es valida"
			Esperar Tecla
			//Esperar 2 Segundos
			Borrar Pantalla
		SiNo
			Escribir "Contraseña valida"
			passValid<-Verdadero
		FinSi
	Fin Mientras	
FinAlgoritmo
