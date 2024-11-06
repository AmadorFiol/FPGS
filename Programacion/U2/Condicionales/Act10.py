#Crear script que pida 3 numeros, mediante condicionales devuelve el mayo de los tres
num1=int(input("Escriba un numero: "))
num2=int(input("Escriba un numero: "))
num3=int(input("Escriba un numero: "))
if(num1>num2 and num1>num3):
    print(num1)
elif(num2>num3):
    print(num2)
else:
    print(num3)