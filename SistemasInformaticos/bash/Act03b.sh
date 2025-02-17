#Inicializacion de variables de argumentos
c=0
p=0
g=0
s=0

#Argumentos
while [ "$#" != "0" ]; do
	case "$1" in
		-c) c=1 ;;
		-p) p=1 ;;
		-g) g=1 ;;
		-s) s=1 ;;
		-a) c=1 ; p=1 ; g=1 ; s=1 ;;
		*) break ;;
	esac
	shift
done
#Inicializacion de variables de calculos
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
if [ "$c" -eq "1" ]; then
	echo "Se han introducido $i numeros"
fi
if [ "$p" -eq "1" ]; then
	echo "El numero menor es $menor"
fi
if [ "$g" -eq "1" ]; then
	echo "El numero mayor es $mayor"
fi
if [ "$s" -eq "1" ]; then
	echo "La suma de todos los numeros es $sum"
fi
