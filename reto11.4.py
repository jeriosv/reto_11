def sumarColumna(matriz, columna):   # Función para sumar los elementos de una columna dada de una matriz
    if columna < 0 or columna >= len(matriz[0]):     # Verificar que la columna sea válida
        print("La columna ingresada no es válida.")
        return None
    suma = 0
    for fila in matriz:       # Sumar los elementos de la columna
        suma += fila[columna]
    return suma

matriz = []
filas =    int(input("Ingrese el número de filas de la matriz:    "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor en la posición ({i}, {j}) : "))
        fila.append(valor)
    matriz.append(fila)

print("Matriz ingresada:")   # Imprimir matriz ingresada
for fila in matriz:
    print(fila)

# Ingreso del usuario la columna a sumar
columna = int(input("Ingrese el número de la columna a sumar: (primera 1, segunda 2, ...): "))

resultadoSuma = sumarColumna(matriz, columna-1)    # Sumar elementos de la columna

print("La suma de los elementos de la columna " +  str(columna) + " es: " + str(resultadoSuma))  # Imprimir resultado