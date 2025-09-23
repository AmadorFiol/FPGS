#-----Act 1----#
def leer_texto(ruta_fichero):
    file=open(ruta_fichero,"r")
    lista=[]
    for line in file.readlines():
        line=line.lower().replace("."," ").replace(","," ").split()
        for word in line:
            lista.append(word)
    return lista
            
#-----Act 2-----#
def calcular_frecuencias(lista_palabras):
    diccionario={}
    for word in lista_palabras:
        if word in diccionario:
            diccionario[word]+=1
        else:
            diccionario[word]=1
    return diccionario

#-----Act 3-----#
def generar_ranking(diccionario_frecuencias,n):
    ranking=[(0,0)]*n
    for word in diccionario_frecuencias:
        for position in range(len(ranking)):
            if diccionario_frecuencias[word]>ranking[position][1]:
                try:
                    ranking[position+1]=ranking[position]
                except IndexError:
                    pass
                ranking[position]=(word,diccionario_frecuencias[word])
                break
    return ranking

#----Act 4----#
def exportar_ranking_csv(ranking, nombre_fichero):
    file=open(f"{nombre_fichero}.csv","w")
    for tupla in ranking:
        file.writelines(f"{tupla[0]},{tupla[1]}\n")
    file.close()
    return f"{nombre_fichero}.csv"

#-----Act 5-----#
def ley_zipf(fichero,n):
    file=open(fichero,"r")
    data=file.readlines()
    file.close()
    file=open(fichero,"w")
    for line in data:
       line=line.replace("\n","").split(",")
       file.writelines(f"{line[0]},{line[1]},{(int(line[1])/n*100)}\n")
    file.close()
#-----Main-----#
lista=leer_texto("file.txt")
print(lista)
diccionario=calcular_frecuencias(lista)
print(diccionario)
lista_tuplas=generar_ranking(diccionario,4)
print(lista_tuplas)
file=exportar_ranking_csv(lista_tuplas,"ranking")
file=ley_zipf(file,len(lista))



