'''
Dentro de cada categoría, recorre los productos.Calcula el valor total de cada producto (cantidad × precio)
Suma el valor total de todos los productos para obtener el valor del inventario completo.
'''
sum=0
inventario = {
    "Electrónica":{
        "Smartphone": {"cantidad": 50, "precio": 699.99},
        "Laptop": {"cantidad": 20, "precio": 999.99},
        "Auriculares": {"cantidad": 100, "precio": 49.99}
    },
    "Hogar":{
        "Sofá": {"cantidad": 10, "precio": 499.99},
        "Mesa": {"cantidad": 15, "precio": 199.99},
        "Silla": {"cantidad": 30, "precio": 89.99}
    },
    "Ropa":{
        "Camiseta": {"cantidad": 200, "precio": 19.99},
        "Pantalón": {"cantidad": 100, "precio": 39.99},
        "Zapatos": {"cantidad": 50, "precio": 79.99}
    }
}

for cat in inventario:
    print("\n",cat)
    sumCat=0
    for prod in inventario[cat]:
        print(prod,":",inventario[cat][prod]["cantidad"]*inventario[cat][prod]["precio"],"€")
        sumCat=sumCat+inventario[cat][prod]["cantidad"]*inventario[cat][prod]["precio"]
        sum=sum+inventario[cat][prod]["cantidad"]*inventario[cat][prod]["precio"]
    print("El total de esta categoria es:",sumCat)
print("\nEl total del inventario es:",sum,"€")