@echo off
REM MyFirstBat esto es un comentario
:bucle
dir
set /p $carpeta="A que carpeta quieres entrar?"
REM Para acceder al valor de una variable hay que poner el nombre entre 2 %
cd %$carpeta%
goto bucle