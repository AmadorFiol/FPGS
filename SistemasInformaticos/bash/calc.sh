echo S. Sumar
echo R. Restar
echo M. Multiplicar
echo D. Dividir
read -p "" input
case $input in
	"S")
	read -p "" x
	read -p "" y
	let resultado=$x+$y
	echo "El resultado de $x + $y es $resultado"
	;;
	"R")
	read -p "" x
        read -p "" y
        let resultado=$x-$y
        echo "El resultado de $x - $y es $resultado"
	;;
	"M")
	read -p "" x
        read -p "" y
        let resultado=$x*$y
        echo "El resultado de $x * $y es $resultado"
	;;
	"D")
	read -p "" x
        read -p "" y
        if [ $y = 0 ]
        then
                echo "No se puede dividir entre 0"
        else
                let resultado=$x/$y
                echo "El resultado de $x / $y es $resultado"
        fi
	;;
	*)
	echo "Esa no es una opcion valida"
	;;
esac
