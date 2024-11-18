@echo off
::Control de errores
if "%1"=="" (
    echo "Uso: comparadorNumeros.bat num1 num2"
    pause
    goto fin
)

if %1 gtr %2 (echo %1 es mayor que %2
) else if %1 lss %2 (echo %2 es mayor que %1
) else (echo Los dos numeros son iguales)

:fin