@echo off
REM V.GoTo
cls REM Limpiar la pantalla
:calc
echo "Calculadora"
echo "S:Sumar"
echo "R:Resta"
echo "M:Multiplicar"
echo "D:Division"
echo "Q:Salir"

set /p input="Que quieres hacer: "
goto %input%

:s
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    set /a z=x+y
    echo "El resultado de la suma de %x% y %y% es %z%"
    pause
    goto calc
:r
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    set /a z=x-y
    echo "El resultado de la resta de %x% y %y% es %z%"
    pause
    goto calc
:m
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    set /a z=x*y
    echo "El resultado de la multiplicacion de %x% y %y% es %z%"
    pause
    goto calc
:d
    set /p x="Di un primer num: "
    set /p y="Di un segundo num: "
    if %y%=="0"(
        echo "No se puede dividir entre 0"
    )else(
        set /a z=x/y
        echo "El resultado de la division de %x% y %y% es %z%"
    )
    pause
    goto calc

:q
    exit

REM <LSS, >GTR, =< LEQ, >= GEQ