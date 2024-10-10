@echo off
REM V.If
cls REM Limpiar la pantalla

echo "Calculadora"
echo "S:Sumar"
echo "R:Resta"
echo "M:Multiplicar"
echo "D:Division"
echo "Q:Salir"

set /p input="Que quieres hacer: "

REM RECUERDA EL PUTO ESPACIO
if "%input%"=="S" (
    set /p x="Di un primer num: "
    echo "%x%"
    set /p y="Di un segundo num: "
    echo "%y%"
    set /a z=x+y
    echo "El resultado de la suma de %x% y %y% es %z%"
    pause
)else if "%input%"=="R" (
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    set /a z=x-y
    echo "El resultado de la resta de %x% y %y% es %z%"
    pause
)else if "%input%"=="M" (
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    set /a z=x*y
    echo "El resultado de la multiplicacion de %x% y %y% es %z%"
    pause
)else if "%input%"=="D" (
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    if "%y%"=="0" (
        echo "No se puede dividir entre 0"
        )else (
            set /a z=x/y
            echo "El resultado de la division de %x% y %y% es %z%"
        )
        pause
)
REM <LSS, >GTR, =< LEQ, >= GEQ