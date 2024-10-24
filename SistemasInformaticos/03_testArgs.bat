@echo off

::Control de errores
if "%1"=="" (
    echo Uso: %0 -arg num1 num2...
    pause
    goto fin
) else if "%2"=="" (
    echo Faltan los numeros
    pause
    goto fin
) else if "%3"=="" (
    echo Falta un segundo numero para realizar las acciones
    pause
    goto fin
)

::Inicializamos variables
    set contar=0
    set min=%2
    set max=%2
    set total=%2

::If's que controlan el argumento y a donde van dirigidos
if "%1"=="-c" (
    shift
    goto c
) else if "%1"=="-p" (
    shift
    goto p
) else if "%1"=="-g" (
    shift
    goto g
) else if "%1"=="-s" (
    shift
    goto s
) else if "%1"=="-a" (
    shift
    goto a
)

::Con shift nos movemos a una posicion a la derecha y luego volvermos a la etiqueta $Arg
::Cuando se agoten las posiciones %1 estara vacio y nos dirigiremos a la etiqueta fin$Arg

::Etiquetas para conteo
:c
if "%1"=="" goto finC
set /a contar=%contar%+1
shift
goto c

:finC
echo Son %contar% numeros
goto fin

::Zona encontrar menor
:p
if "%1"=="" goto finP
if %1 lss %min% set min=%1
shift
goto p

:finP
echo El numero mas pequeno es %min%
goto fin

::Encontrar mayor
:g
if "%1"=="" goto finG
if %1 gtr %max% set max=%1
shift
goto g

:finG
echo El numero mas grande es %max%
goto fin

::Sumatorio
:s
if "%1"=="" goto finS
set /a total=%total%+%1
shift
goto s

:finS
echo El total es: %total%
goto fin

::Zona todos
:a
if "%1"=="" goto finA
set /a contar=%contar%+1
if %1 lss %min% set min=%1
if %1 gtr %max% set max=%1
set /a total=%total%+%1
shift
goto a

:finA
echo Son %contar% numeros
echo El numero mas pequeno es %min%
echo El numero mas grande es %min%
echo El total es: %total%

:fin
