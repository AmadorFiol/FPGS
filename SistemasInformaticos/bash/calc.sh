echo S. Sumar
echo R. Restar
echo M. Multiplicar
echo D. Dividir
read -p "" input
if [ $input = "S" ]
then
	read -p "" x
	read -p "" y
	let resultado=$x+$y
	echo "El resultado de $x + $y es $resultado"
fi
if [ $input = "R" ]
then
	read -p "" x
	read -p "" y
	let resultado=$x-$y
	echo "El resultado de $x - $y es $resultado"
fi
if [ $input = "M" ]
then
	read -p "" x
	read -p "" y
	let resultado=$x*$y
	echo "El resultado de $x * $y es $resultado"
fi
if [ $input = "D" ]
then
	read -p "" x
	read -p "" y
	if [ $y = 0 ]
	then
		echo "No se puede dividir entre 0"
	else
		let resultado=$x/$y
		echo "El resultado de $x / $y es $resultado"
	fi
fi
