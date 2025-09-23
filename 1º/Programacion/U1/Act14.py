#Define una función que reciba un nombre como parámetro y que haga una concatenación de 2 frases y luego las imprimirla por pantalla.

def WriteConcatYNombre(nombre):
    fraseCompleta="Hola "+nombre+". Encantado de conocerte"
    print(fraseCompleta)

nombre=input("Escribe un nombre: ")
WriteConcatYNombre(nombre)