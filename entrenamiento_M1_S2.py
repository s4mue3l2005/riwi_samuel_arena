def promedio_notas():
    while True:
        try:
            nota = float(input("ingrese su calificacion entre 0 y 100: "))
            if 0<= nota <= 100:
                return nota
            else:
                print("su calificacion tiene que se entre 0 y 100")
        except ValueError:
            print("entrada no valida, ingrese un numero")
def estado_aprobacion(nota,nombre):
    if nota >= 60:
        print(f"{nombre} felicidades has aprobado. ")
    else:
        print(f"{nombre} no aprobado. ")   
def lista_de_calificaciones():
    while True:
        entrada = input("ingresa tres calificaciones separadas por comas (ej. 30,80,70)")
        try:
            lista = [float(nota.strip()) for nota in entrada.split(",") if 0 <= float(nota.strip()) <= 100]
            if lista:
                return lista
            else:
                print("Todas las calificaciones deben estar entre 0 y 100.")
        except ValueError:
            print("Error: asegúrate de usar solo números válidos y separados por comas.")
def calculadora_de_promedio(lista):
    suma = 0
    for nota    in lista:
        suma += nota
    promedio = suma/ len(lista)
    print(f"El promedio de las calificaciones es{promedio:.2f}")
    return promedio
def contar_mayor_que(lista, valor):
    contador=0
    i=0
    while i < len (lista):
        if lista[i]>valor:
            contador +=1
        i+=1
    print(f"Hay {contador} calificaciones mayores que {valor}.")
def contar_calificaciones_espesifica(lista, objetivo):
    contador = 0
    for nota in lista:
        if nota == objetivo:
            contador +=1
            continue
        if nota < 0:
            break
    print(f"La calificacion{objetivo} aparece {contador} veces en la lista.")

# encabezado 
print ("Bienvenido al gestor de calificaciones \n")

nombre_estudiante = input("porfavor, ingresa el nombre del estudiante: ").strip().title()
nota_individual= promedio_notas()
lista_notas = lista_de_calificaciones()
estado_aprobacion(nota_individual, nombre_estudiante)
try:
    valor_comparar = float(input("Ingresa un valor para contar cuántas calificaciones son mayores: "))
    contar_mayor_que(lista_notas, valor_comparar)
except ValueError:
    print("Valor no válido.")

# Verificar cuántas veces aparece una calificación específica
try:
    valor_objetivo = float(input("Ingresa una calificación específica a buscar en la lista: "))
    contar_calificaciones_espesifica(lista_notas, valor_objetivo)
except ValueError:
    print("Valor no válido.")

print(f"\nFin del programa. ¡Gracias, {nombre_estudiante}, por usar el gestor de calificaciones!")
