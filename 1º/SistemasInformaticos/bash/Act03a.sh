#Inicializacion de variables
mayor=$1
menor=$1
i=0
sum=0
#Bucle principal
while [ "$#" -gt "0" ]; do
	let i=$i+1
	let sum=$sum+$1
	#Comparacion
	if [ $1 -gt $mayor ]; then
		mayor=$1
	elif [ $1 -lt $menor ]; then
		menor=$1
	fi
	shift
done
#Mostrado de mensajes
echo "Se han introducido $i numeros"
echo "El numero menor es $menor"
echo "El numero mayor es $mayor"
echo "La suma de todos los numeros es $sum"
