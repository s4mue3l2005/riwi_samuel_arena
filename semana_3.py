# Diccionario que almacena los productos: nombre -> (precio, cantidad)
inventario = {}

# Función para mostrar el menú y recibir la opción del usuario
def mostrar_menu():
    """Muestra el menú principal y gestiona la selección del usuario."""
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar inventario completo")
        print("7. Salir")

        # Recibimos la opción del usuario
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == '1':
            # Añadir un producto
            nombre = input("Ingrese el nombre del producto: ")
            while True:
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    if precio < 0:
                        print("Error: El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Error: El precio debe ser un número válido.")
            
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    if cantidad < 0:
                        print("Error: La cantidad no puede ser negativa.")
                        continue
                    break
                except ValueError:
                    print("Error: La cantidad debe ser un número entero.")
                
            añadir_producto(nombre, precio, cantidad)
            input("Presiona Enter para continuar...")

        elif opcion == '2':
            # Consultar un producto
            nombre = input("Ingrese el nombre del producto a consultar: ")
            consultar_producto(nombre)
            input("Presiona Enter para continuar...")

        elif opcion == '3':
            # Actualizar el precio de un producto
            nombre = input("Ingrese el nombre del producto para actualizar su precio: ")
            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio < 0:
                        print("Error: El precio no puede ser negativo.")
                        continue
                    break
                except ValueError:
                    print("Error: El precio debe ser un número válido.")
                
            actualizar_precio(nombre, nuevo_precio)
            input("Presiona Enter para continuar...")

        elif opcion == '4':
            # Eliminar un producto
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(nombre)
            input("Presiona Enter para continuar...")

        elif opcion == '5':
            # Calcular el valor total del inventario
            total = calcular_total_inventario()
            print(f"\nEl valor total del inventario es: {total:.2f}\n")
            input("Presiona Enter para continuar...")

        elif opcion == '6':
            # Mostrar el inventario completo
            mostrar_inventario()
            input("Presiona Enter para continuar...")

        elif opcion == '7':
            # Salir del programa
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida. Por favor, ingresa una opción válida (1-7).")

# Función para añadir un producto al inventario
def añadir_producto(nombre, precio, cantidad):
    """Añade un producto al inventario si no existe previamente."""
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe en el inventario.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"\nProducto '{nombre}' añadido con éxito.\n")

# Función para consultar los detalles de un producto
def consultar_producto(nombre):
    """Consulta los detalles de un producto por su nombre."""
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"\nProducto: {nombre}\nPrecio: {precio}\nCantidad disponible: {cantidad}\n")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.\n")

# Función para actualizar el precio de un producto existente
def actualizar_precio(nombre, nuevo_precio):
    """Actualiza el precio de un producto en el inventario."""
    if nombre in inventario:
        cantidad = inventario[nombre][1]  # Obtenemos la cantidad
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"\nEl precio de '{nombre}' ha sido actualizado a {nuevo_precio}.\n")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.\n")

# Función para eliminar un producto del inventario
def eliminar_producto(nombre):
    """Elimina un producto del inventario."""
    if nombre in inventario:
        del inventario[nombre]
        print(f"\nProducto '{nombre}' eliminado del inventario.\n")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.\n")

# Función para calcular el valor total del inventario
def calcular_total_inventario():
    """Calcula el valor total del inventario utilizando una función lambda."""
    return sum(precio * cantidad for precio, cantidad in inventario.values())

# Función para mostrar el inventario completo
def mostrar_inventario():
    """Muestra todos los productos en el inventario."""
    if inventario:
        print("\n--- Inventario Actual ---")
        for nombre, (precio, cantidad) in inventario.items():
            print(f"Producto: {nombre}, Precio: {precio}, Cantidad: {cantidad}")
        print("\n")
    else:
        print("\nEl inventario está vacío.\n")

# Función principal para iniciar el programa
def main():
    """Función principal para iniciar la gestión del inventario."""
    mostrar_menu()

# Ejecutamos el programa
if __name__ == "__main__":
    main()
