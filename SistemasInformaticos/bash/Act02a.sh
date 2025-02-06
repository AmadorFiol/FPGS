num1=$1
num2=$2

if [ $num1 -gt $num2 ]; then
	echo "$num1 es mayor que $num2"
else if [ $num1 -lt $num2 ]; then
	echo "$num2 es mayor que $num1"
else
	echo "$num1 y $num2 son iguales"
fi
fi
