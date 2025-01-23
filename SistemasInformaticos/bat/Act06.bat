@echo off

:loop
if "%1"=="" goto fin
set /a resto=%1 %% 2
if %resto%==0 (
    echo El numero %1 es par
) else (
    echo El numero %1 es impar
)
shift
goto loop

:fin