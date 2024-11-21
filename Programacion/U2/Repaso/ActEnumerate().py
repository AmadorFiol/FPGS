'''
Se ha de usar la funcion enumerate()
Crear lista con los meses del año y
Recorrer la lista indicando que numero de mes es cada elemento
'''
meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
for num,mes in enumerate(meses):
    print(num,"-",mes)