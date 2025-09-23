palabra=input("Dime un palindromo: ")
alReves=""
for caracter in palabra:
    alReves=caracter+alReves
    
#Tambien se puede hacer palabra[::-1] para que te comience a recorrer([::$num]) desde el ultimo caracter([-1]) hasta el primero
#para asi no necesitar el bucle for
if palabra==alReves:
    print("Correcto,",palabra," es un palindromo")
else:
    print("Inconrreto,",palabra," NO es un palindromo")
    print("Un palindromo es una palabra que se lee igual de derecha a izquierda o de izquierda a derecha (Ej. 'Oso')")