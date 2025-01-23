@echo off
set /a resto=%1 %% 2
if %resto%==0 (
    echo El numero %1 es par
) else (
    echo El numero %1 es impar
)