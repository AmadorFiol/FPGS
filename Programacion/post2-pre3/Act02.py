'''
Usando un bucles
Crear un array cuyos valores vayan de 1 al 10
Crear diccionario cuya clave sea del 0 al 9
y valores 1 al 10 usando un bucle
'''
array=[]
diccionario={}
for i in range(0,10):
    array.append(i+1)
    diccionario[i]=i+1
print("Array:\n",array,"\n\nDiccionario:\n",diccionario)


