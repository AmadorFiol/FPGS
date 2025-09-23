#Crear script que dado los numeros del DNI devuelva la letra correspondiente
LETRAS=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
numsDNI=int(input("Dime los numeros de tu DNI: "))
restoNumsDNI=numsDNI%23
print("La letra de tu DNI es: ",LETRAS[restoNumsDNI])