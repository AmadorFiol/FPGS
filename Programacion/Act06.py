#Enunciado: Pedir dos datos, almacenarlos en dos variables distintas.
#Intercambiar los valores (realizar un swap) e imprimir los valores de las variables
x=input("Escribe un numero (x): ")
y=input("Escribe otro numero (y): ")

x,y=y,x

print("He invertido el valor de las variables, ahora x es", x,"e y ahora es", y)