@echo off

::Control de errores
if "%1"=="" (
    echo Uso: %0 -args num1 num2...
    echo Los argumentos son:
    echo -c para contar los numeros
    echo -p para encontrar el numero mas pequeno
    echo -g para encontrar el numero mas grande
    echo -s para realizar la suma de todos los numeros
    echo -a para realizar todas las anteriores
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

::Bucle para comprobar los argumentos
:argumentos
if "%1"=="-c" (
    shift
    set c=1
    goto argumentos
) else if "%1"=="-p" (
    shift
    set p=1
    goto argumentos
) else if "%1"=="-g" (
    shift
    set g=1
    goto argumentos
) else if "%1"=="-s" (
    shift
    set s=1
    goto argumentos
) else if "%1"=="-a" (
    shift
    set c=1
    set p=1
    set g=1
    set s=1
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

::Se muestran los mensajes correspondientes al de los argumentos pasados por el usuario
:mensajes
if %c%==1 (
    echo Son %contar% numeros
)
if %p%==1 (
    echo El numero mas pequeno es %min%
)
if %g%==1 (
    echo El numero mas grande es %max%
)
if %s%==1 (
    echo El total es: %total%
)

:fin