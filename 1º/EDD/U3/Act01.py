class Producto:
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio


class Cliente:
    def __init__(self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo

class Pedido:
    def __init__(self, productos, cantidadProds, cliente):
        self.productos=productos
        self.cantidadProds=cantidadProds
        self.cliente=cliente
    
    def calcular_total(self):
        total=0
        for i,producto in enumerate(self.productos):
            total+=self.cantidadProds[i]*producto.precio  # cantidad * precio_unitario
        return total
    
    def aplicar_descuento(self):
        total=self.calcular_total()
        if self.cliente.tipo==TIPOSCLIENTES[1]:
            total*=0.9 #10% de descuento
        elif self.cliente.tipo==TIPOSCLIENTES[2]:
            total*=0.95 #5% de descuento
        return total
#Chistoso lo del copy, buen truco si no leen el codigo antes
    def generar_factura(self):
        factura=f"Factura para {self.cliente.nombre}:\n"
        for i,producto in enumerate(self.productos):
            factura+=f"{producto.nombre} - {self.cantidadProds[i]} x ${producto.precio} = ${self.cantidadProds[i]*producto.precio}\n"
        factura+=f"Total: ${self.calcular_total()}\n"
        return factura

# Uso 
TIPOSCLIENTES=["Basico","VIP","Frecuente"]
productos=[Producto("Laptop", 1000),Producto("Raton",25)]
clientes=[Cliente("Carlos",TIPOSCLIENTES[1])]
pedido=Pedido([productos[0],productos[1]],[1,2], clientes[0])
print(pedido.generar_factura())
print("Total con descuento VIP:", pedido.aplicar_descuento())
