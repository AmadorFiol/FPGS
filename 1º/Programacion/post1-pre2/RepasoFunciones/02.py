#Escribir una función que reciba una lista con 2 números y devuelva un diccionario con el mayor, menor, media
def orderNum(parametro):
    diccionario={"mayor":max(parametro),"menor":min(parametro),"media":sum(parametro)/len(parametro)}
    print("El numero mas grande es: ",diccionario["mayor"],"el numero menor es: ",diccionario["menor"],"y la media es: ",diccionario["media"])

array=[45,25]

orderNum(array)