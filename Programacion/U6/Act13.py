def gestionar_inventario():
    inventario = {
        "manzanas": 10,
        "bananas": 15,
        "naranjas": 8
    }

    while True:
        print("Opciones:")
        print("1. Consultar stock")
        print("2. Agregar unidades")
        print("3. Restar unidades")
        print("4. Salir")

        match(input("Selecciona una opción (1-4): ")):
            case "1":
                producto = input("Ingresa el nombre del producto: ").lower()
                try:
                    print(f"Stock de {producto}: {inventario[producto]}")
                except KeyError:
                    print("Error: El producto no existe en el inventario.")

            case "2":
                producto = input("Producto al que deseas agregar unidades: ").lower()
                if producto in inventario:
                    try:
                        cantidad = int(input("Cantidad a agregar: "))
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor que cero.")
                        else:
                            inventario[producto] += cantidad
                            print(f"Se agregaron {cantidad} unidades a {producto}. Nuevo stock: {inventario[producto]}")
                    except ValueError:
                        print("Error: Ingresa un número entero válido.")
                else:
                    print("Error: El producto no existe en el inventario.")

            case "3":
                producto = input("Producto al que deseas restar unidades: ").lower()
                if producto in inventario:
                    try:
                        cantidad = int(input("Cantidad a restar: "))
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor que cero.")
                        elif cantidad > inventario[producto]:
                            print("Error: No hay suficiente stock para restar esa cantidad.")
                        else:
                            inventario[producto] -= cantidad
                            print(f"Se restaron {cantidad} unidades a {producto}. Nuevo stock: {inventario[producto]}")
                    except ValueError:
                        print("Error: Ingresa un número entero válido.")
                else:
                    print("Error: El producto no existe en el inventario.")

            case "4":
                print("Saliendo del programa.")
                break

            case _:
                print("Opción no válida. Intenta de nuevo.")


gestionar_inventario()
