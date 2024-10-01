#Solicitar tres numeros almacenarlos en variables diferentes y realizar la suma, multiplicacion
#resta y division de ellos en el orden que quieras
x=int(input("Escribe un numero: "))
y=int(input("Escribe otro numero: "))
z=int(input("Escribe otro numero mas: "))

res=x+y+z
print("La suma de los 3 numeros es: ",res)
res=x-y-z
print("La resta de los 3 numeros es: ",res)
res=x*y*z
print("La multiplicacion de los 3 numeros es: ",res)
res=(x/y)/z
print("La division de los 3 numeros es: ",res)