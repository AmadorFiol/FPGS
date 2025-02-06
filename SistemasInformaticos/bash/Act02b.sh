num1=$1
num2=$2

#Control de errores
if [ -z $num1 ]; then
	echo "No se ha introducido ningun argumento"
else if [ -z $num2 ]; then
	echo "Falta un segundo parametro"
else
	#Comparacion
	if [ $num1 -gt $num2 ]; then
		echo "$num1 es mayor que $num2"
	else if [ $num1 -lt $num2 ]; then
		echo "$num1 es menor que $num2"
	else
		echo "$num1 y $num2 son iguales"
	fi
	fi
fi
fi
