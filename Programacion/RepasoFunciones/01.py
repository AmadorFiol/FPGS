#Crear funcion que muestre 3 numeros de un array y devuelva otra listra con sus cuadrados
def mostrarNum(parametro):
    cuadrados=[]
    j=0
    for i in parametro:
        cuadrados.append(i**2)
        print("El cuadrado de ",parametro[j],"es ",cuadrados[j])
        j=j+1
    
array=[2,3,4]
mostrarNum(array)