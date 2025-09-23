@echo off

::Control de errores
if "%1"=="" (
    echo Uso: %0 -args num1 num2...
    pause
    goto fin
) else if "%2"=="" (
    echo Falta otro numero para poder realizar las comparaciones
    pause
    goto fin
)

::Inicializamos variables
set contar=0
set min=%1
set max=%1
set total=%1

::Se realizan los calculos de todos
:loop
if "%1"=="" goto mensajes
set /a contar=%contar%+1
if %1 lss %min% set min=%1
if %1 gtr %max% set max=%1
set /a total=%total%+%1
shift
goto loop

::Mostrar mensajes
:mensajes
echo Son %contar% numeros
echo El numero mas pequeno es %min%
echo El numero mas grande es %max%
echo El total es: %total%

:fin