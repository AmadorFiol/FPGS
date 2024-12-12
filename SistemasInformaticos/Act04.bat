@echo off
if "%1"=="" (
    echo "%0 -arg1 -arg2... num1 num2..."
    echo "Argumentos:"
    echo "-b para pasar a binario"
    echo "-o para pasar a octal"
    echo "-d para pasar a decimal"
    echo "-h para pasar a hexadecimal"
    goto fin
)
set b=0
set o=0
set d=0
set h=0
:parametro
if "%1"=="-b":
    set b=1
    shift
    goto parametro
if "%1"=="-o":
    set o=1
    shift
    goto parametro
if "%1"=="-d":
    set d=1
    shift
    goto parametro
if "%1"=="-h":
    set h=1
    shift
    goto parametro
if "%1"=="-a":
    set b=1
    set o=1
    set d=1
    set h=1
    shift
    goto parametro

if "%1"=="" (
    echo "No hay numeros"
    goto fin
)
:loop
if "%1"=="" goto fin
set num=%1
if %b%=1 (
    set binNum=0
    set actualNum=-1
    :binario
    set lastDigit=%num:~(%actualNum%)%
    set binDigitToChek=%binNum:~-1%

    if %lastDigit%==1 (
        if %binDigitToChek%==0 (
            set /a binNum=%binNum%+1
        )
        if %binDigitToChek%==1 (
            set /a binNum=%binNum%+9
        )
    )

    if %lastDigit%==2()
    if %lastDigit%==3()
    if %lastDigit%==4()
    if %lastDigit%==5()
    if %lastDigit%==6()
    if %lastDigit%==7()
    if %lastDigit%==8()
    if %lastDigit%==9()

    set /a actualNum=%actualNum%-1
    goto binario
)

if %o%=1 ()
if %d%=1 ()
if %h%=1 ()
shift
goto loop

:fin