def calcular_costo_total():
    nombre_producto = input("Introduce el nombre del producto: ")
#validamos el precio unotario
    while True:
        try:
            precio_unitario = float(input("Introduce el precio unitario del producto: "))
            if precio_unitario <= 0:
                print("El precio unitario debe ser un valor positivo. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el precio unitario.")
#validamos la cantidad de productos
    while True:
        try:
            cantidad = int(input("Introduce la cantidad de productos adquiridos: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número entero positivo. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido para la cantidad.")
#solicitamos el porcentaje de descuento y validamos si es negativo 
    while True:
        try:
            descuento = float(input("Introduce el porcentaje de descuento (si no hay descuento, ingresa 0): "))
            if descuento < 0:
                print("El descuento no puede ser negativo. Se considerará 0.")
                descuento = 0  # Si el descuento es negativo, lo corregimos a 0
                break
            elif descuento > 100:
                print("El descuento no puede ser mayor al 100%. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el descuento.")
    # hacemos las operaciones
    costo_sin_descuento = precio_unitario * cantidad
    monto_descuento = (descuento / 100) * costo_sin_descuento
    costo_total = costo_sin_descuento - monto_descuento
    # Mostramos el resumen de la compra
    print("\nResumen de la compra:")
    print(f"Producto: {nombre_producto}")
    print(f"Costo sin descuento: ${costo_sin_descuento:.2f}")
    print(f"Descuento aplicado: ${monto_descuento:.2f}")
    print(f"Costo total a pagar: ${costo_total:.2f}") 
    # Preguntamos si el usuario desea hacer otro cálculo
    continuar = input("\n¿Deseas realizar otra compra? (sí/no): ").strip().lower()
    if continuar == 'sí' or continuar == 'si':
        calcular_costo_total()  # Llamamos de nuevo a la función para continuar el cálculo
    else:
        print("Gracias por usar el sistema de compras.")
calcular_costo_total()