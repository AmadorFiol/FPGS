#Escribir una función que reciba una lista con 2 números y devuelva un diccionario con el mayor, menor, media
def orderNum(parametro):
    if(parametro[0]>parametro[1]):
        diccionario={"mayor":parametro[0],"menor":parametro[1],"media":(parametro[0]+parametro[1])/len(parametro)}
    else:
        diccionario={"mayor":parametro[1],"menor":parametro[0],"media":(parametro[0]+parametro[1])/len(parametro)}

    print("El numero mas grande es: ",diccionario["mayor"],"el numero menor es: ",diccionario["menor"],"y la media es: ",diccionario["media"])

array=[45,25]

orderNum(array)