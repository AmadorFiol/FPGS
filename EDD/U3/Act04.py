class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre if nombre else "Producto sin nombre"
        self.precio = precio
        self.stock = stock 

    def mostrar_informacion(self):
        if self.precio < 0 or self.stock < 0:
            print(f"Producto '{self.nombre}' tiene datos incorrectos.")
        else:
            print(f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def aplicar_descuento(self, descuento):
        if descuento>100:
            print("Descuento superior al 100% no permitido")
        elif descuento<0:
            print("Descuento negativo no permitido")
        else:
            self.precio -= self.precio * (descuento / 100)


class TodoList:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, producto):
        if not isinstance(producto, Producto):
            print("Error: Solo se pueden agregar objetos de tipo Producto.")
        else:
            self.tareas.append(producto)

    def eliminar_tarea(self, nombre_producto):
        for tarea in self.tareas:
            if tarea.nombre == nombre_producto:
                self.tareas.remove(tarea)
                print(f"Producto '{nombre_producto}' encontrado, se procede la eliminacion.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for tarea in self.tareas:
                tarea.mostrar_informacion()


# Ejemplo de uso de las clases con errores
todo_list = TodoList()

# Productos con datos incorrectos
producto1 = Producto("Laptop", 1000, 10)  # Producto válido
producto2 = Producto("Smartphone", 500, 5)  # Producto válido (Precio ahora positivo)
producto3 = Producto("Tablet", 300, 3)  # Producto válido (Stock ahora positivo)
producto4 = Producto("Cargador", 200, 20)  # Producto válido (Agregado nombre)

# Agregar productos a la lista de tareas
todo_list.agregar_tarea(producto1)  # Producto válido
todo_list.agregar_tarea(producto2)  # Producto válido (Solucionado error precio)
todo_list.agregar_tarea(producto3)  # Producto válido (Solucionado error stock)
todo_list.agregar_tarea(producto4)  # Producto válido (Solucionado error nombre)

# Mostrar todas las tareas
todo_list.mostrar_tareas()

# Intentar eliminar un producto de la lista
todo_list.eliminar_tarea("Laptop")  # Eliminacion correcta (El metodo ya no setea el stock a 0)
todo_list.eliminar_tarea("Cargador")  # Eliminacion correcta (Cargador ahora si esta como producto)
todo_list.mostrar_tareas()  # Mostrar después de intentar la eliminación

# Aplicar descuento erróneo a un producto
producto1.aplicar_descuento(150)  # Metodo ahora tiene en cuenta descuentos superiores a 100 o inferiores a 0
producto2.aplicar_descuento(20)  # Aplicar descuento correctamente
todo_list.mostrar_tareas()  # Ver los cambios
