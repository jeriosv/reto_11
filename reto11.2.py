def ingresarMatriz(filas, columnas):  # Función para ingresar valores de la matriz
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicarMatrices(m1, m2):  # Función que multiplica dos matrices
    f1 = len(m1)
    c2 = len(m2[0])
    resultado = [[0] * c2 for i in range(f1)]
    for i in range(f1):
        for j in range(c2):
            for k in range(len(m2)):
                resultado[i][j] += m1[i][k] * m2[k][j]
    return resultado

# Ingreso del usuario de las matrices
f1 = int(input("Ingrese el número de filas de la matriz No. 1:    "))
c1 = int(input("Ingrese el número de columnas de la matriz No. 1: "))
m1 = ingresarMatriz(f1, c1)

f2 = int(input("Ingrese el número de filas de la matriz No. 2:    "))
c2 = int(input("Ingrese el número de columnas de la matriz No. 2: "))
m2 = ingresarMatriz(f2, c2)

print("Matriz 1:")    # Imprimir matriz 1
for fila in m1:
    print(fila)

print("Matriz 2:")    # Imprimir matriz 2
for fila in m2:
    print(fila)

if c1 != f2:
    print("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz. No se pueden multiplicar las matrices.")
else:
    resultado = multiplicarMatrices(m1, m2)     # Multiplicar las matrices
    print("La matriz resultado del producto:")  # Imprimir la matriz resultado
    for fila in resultado:
        print(fila)