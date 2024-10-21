@echo off

::Inicializamos variables
set contar=0
set total=0
set min=%1
set max=%1

::Control de errores
if "%1"=="" (
    echo Uso: %0 num1 num2
    pause
    goto fin
) else if "%2"=="" (
    echo Falta un segundo numero para la comparacion
    pause
    goto fin
)

::Iteracion que hace "todo"
:loop

::Cuando se agoten las posicione %1 estara vacio y nos dirigiremos a la etiqueta hecho
if "%1"=="" goto hecho
set /a contar=%contar%+1
set /a total=%total%+%1

if %1 lss %min% set min=%1

if %1 gtr %max% set max=%1

::Con shift nos movemos a una posicion a la derecha y luego volvermos a la etiqueta loop
shift
goto loop

:hecho
echo El total es: %total%
echo Son %contar% numeros
echo El numero mas pequeno es %min%
echo El numero mas grande es %max%
:fin
