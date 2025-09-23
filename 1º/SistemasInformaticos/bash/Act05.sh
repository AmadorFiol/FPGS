if [ -z $1 ]; then
	echo "No se han pasado parametros"
else 
	let resto=$1%2;
	if [ "$resto" == "0" ]; then
		echo "El numero $1 es par"
	else
		echo "El numero $1 es impar"
	fi
fi
