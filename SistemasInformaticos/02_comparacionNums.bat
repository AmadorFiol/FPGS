@echo off
::Control de errores
if "%1"=="" (
    echo "Uso: comparadorNumeros.bat num1 num2"
    pause
    goto fin
)

set num1=%1
set num2=%2
if %num1% gtr %num2% (echo %num1% es mayor que %num2%
) else if %num1% lss %num2% (echo %num2% es mayor que %num1%
) else (echo Los dos numeros son iguales)

:fin