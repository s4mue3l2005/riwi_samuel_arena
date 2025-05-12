# Inventario y registro de ventas
productos = {}
ventas = []
contador_ventas = 1
CLAVE_TRABAJADOR = "clave123"

# ========= FUNCIONES PRINCIPALES =========

def iniciar_sistema():
    while True:
        print("\n🚀 BIENVENIDO A LA TIENDA DE TECNOLOGÍA")
        print("1. Soy Cliente")
        print("2. Soy Trabajador")
        print("3. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            menu_cliente()
        elif eleccion == "2":
            menu_trabajador()
        elif eleccion == "3":
            print("👋 Gracias por usar el sistema.")
            break
        else:
            print("❌ Opción inválida.")

# ========= MENÚ CLIENTE =========

def menu_cliente():
    print("\n👤 MENÚ CLIENTE")
    id_cliente = input("Ingrese su ID de cliente (solo números): ")
    if not id_cliente.isdigit():
        print("❌ El ID del cliente debe contener solo números.")
        return

    while True:
        print("\n1. Comprar productos")
        print("2. Ver mis compras")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_inventario()
            codigos = input("Ingrese los códigos de productos separados por comas: ").split(",")
            codigos = [c.strip() for c in codigos]
            registrar_venta(id_cliente, codigos)
        elif opcion == "2":
            consultar_ventas_por_cliente(id_cliente)
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida.")

# ========= MENÚ TRABAJADOR =========

def menu_trabajador():
    clave = input("Ingrese la clave de trabajador: ")
    if clave != CLAVE_TRABAJADOR:
        print("❌ Clave incorrecta.")
        return

    while True:
        print("\n👨‍💻 MENÚ TRABAJADOR")
        print("1. Registrar producto")
        print("2. Consultar inventario")
        print("3. Consultar ventas por cliente")
        print("4. Buscar productos por categoría")
        print("5. Calcular total de ventas por categoría")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del producto: ")
            if codigo in productos:
                print("❌ Este código ya existe.")
                continue
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                if precio < 0:
                    raise ValueError
            except ValueError:
                print("❌ Precio inválido. Debe ser un número positivo.")
                continue
            categoria = input("Categoría: ")
            registrar_producto(codigo, nombre, precio, categoria)

        elif opcion == "2":
            consultar_inventario()
        elif opcion == "3":
            cliente_id = input("ID del cliente (solo números): ")
            if not cliente_id.isdigit():
                print("❌ El ID debe contener solo números.")
                continue
            consultar_ventas_por_cliente(cliente_id)
        elif opcion == "4":
            categoria = input("Categoría: ")
            buscar_productos_por_categoria(categoria)
        elif opcion == "5":
            categoria = input("Categoría: ")
            calcular_total_ventas_por_categoria(categoria)
        elif opcion == "6":
            break
        else:
            print("❌ Opción inválida.")

# ========= FUNCIONES DE OPERACIÓN =========

def registrar_producto(codigo, nombre, precio, categoria):
    if codigo in productos:
        print(f"❌ Error: El producto con código '{codigo}' ya existe.")
    elif precio < 0:
        print("❌ Error: El precio debe ser un número positivo.")
    else:
        productos[codigo] = (nombre, float(precio), categoria)
        print(f"✅ Producto '{nombre}' registrado con éxito.")

def registrar_venta(id_cliente, codigos_productos):
    global contador_ventas
    for codigo in codigos_productos:
        if codigo not in productos:
            print(f"❌ Error: Producto con código '{codigo}' no existe.")
            return
    total = sum(productos[codigo][1] for codigo in codigos_productos)
    venta = (contador_ventas, id_cliente, codigos_productos, total)
    ventas.append(venta)
    print(f"✅ Venta registrada: ID {contador_ventas}, Total: ${total:.2f}")
    contador_ventas += 1

def consultar_inventario():
    if not productos:
        print("📦 Inventario vacío.")
    else:
        print("📦 Inventario de productos:")
        for codigo, (nombre, precio, categoria) in productos.items():
            print(f"🔹 Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}, Categoría: {categoria}")

def consultar_ventas_por_cliente(id_cliente):
    ventas_cliente = [venta for venta in ventas if venta[1] == id_cliente]
    if not ventas_cliente:
        print(f"❌ No hay ventas registradas para el cliente '{id_cliente}'.")
    else:
        print(f"🧾 Ventas del cliente '{id_cliente}':")
        for id_venta, _, codigos, total in ventas_cliente:
            nombres = [productos[codigo][0] for codigo in codigos]
            print(f"🛒 Venta ID: {id_venta}, Productos: {nombres}, Total: ${total:.2f}")

def buscar_productos_por_categoria(categoria):
    encontrados = [(codigo, info) for codigo, info in productos.items() if info[2].lower() == categoria.lower()]
    if not encontrados:
        print(f"❌ No hay productos en la categoría '{categoria}'.")
    else:
        print(f"📂 Productos en la categoría '{categoria}':")
        for codigo, (nombre, precio, _) in encontrados:
            print(f"🔹 Código: {codigo}, Nombre: {nombre}, Precio: ${precio:.2f}")

def calcular_total_ventas_por_categoria(categoria):
    total = 0.0
    for _, _, codigos, _ in ventas:
        for codigo in codigos:
            if productos[codigo][2].lower() == categoria.lower():
                total += productos[codigo][1]
    print(f"💰 Total de ventas en categoría '{categoria}': ${total:.2f}")

# ========= EJECUCIÓN DEL SISTEMA =========

iniciar_sistema()
