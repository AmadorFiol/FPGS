#Nunca hemos hecho una actividad tratando diccionarios asi que no se como obtener los valores de ellos
def mostrar_stock(producto):
    print("En el almacen hay ",producto.cantidadStock," stock del producto ", producto.nombreProd," a ", producto.precioProd,"/u.")
    print("El total de este producto es: ",producto.cantidadStock*producto.precioProd)

def valor_almacen():
    total=(P1.cantidadStock*P1.precioProd)+(P2.cantidadStock*P2.precioProd)+(P3.cantidadStock*P3.precioProd)+(P4.cantidadStock*P4.precioProd)+(P5.cantidadStock*P5.precioProd)
    print(total)

P1={'nombreProd':"RAM_4Gb",'cantidadStock':5,"precioProd":32.5}
P2={'nombreProd':"RAM_8Gb",'cantidadStock':2,"precioProd":54}
P3={'nombreProd':"CPU_i3",'cantidadStock':6,"precioProd":125}
P4={'nombreProd':"CPU_i5",'cantidadStock':1,"precioProd":224}
P5={'nombreProd':"CPU_i7",'cantidadStock':7,"precioProd":340}

print("Que producto quieres ver?")
print("1. RAM 4Gb")
print("2. RAM 8Gb")
print("3. CPU i3")
print("4. CPU i5")
print("5. CPU i7")
print("6. Total")
match(input()):
    case 1:
        mostrar_stock(P1)
    case 2:
        mostrar_stock(P2)
    case 3:
        mostrar_stock(P3)
    case 4:
        mostrar_stock(P4)
    case 5:
        mostrar_stock(P5)
    case 6:
        valor_almacen()
    case _:
        print("Valor incorrecto")