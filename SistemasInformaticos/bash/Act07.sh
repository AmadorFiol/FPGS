#Inicializacion variables argumentos
e=0
c=0
p=0
i=0

#Argumentos
if [ "$#" != "-e" -o "$#" != "-c" -o "$#" != "-p" -o "$#" != "-i" ]; then
	e=1
	noCoincidences=1
fi

while [ "$#" != "0" ]; do
	if [ $noCoincidences -eq 0 ]; then
		case "$1" in
			-e) e=1;;
			-c) c=1;;
			-p) p=1;;
			-i) i=1;;
			*) break;;
		esac
		shift
	else
		break
	fi
done
#Bucle principal
if [ -z $1 ]; then
	echo "No se han pasado parametros"
else 
	while [ "$#" -gt "0" ]; do
		let resto=$1%2;
		if [ "$resto" == "0" ]; then
			echo "El numero $1 es par"
		else
			echo "El numero $1 es impar"
		fi
		shift
	done
fi
