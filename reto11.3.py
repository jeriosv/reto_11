def matrizTranspuesta(m):    # Función que hace una matriz transpuesta
    resultado = []    
    for j in range(len(m[0])):
        fila = []
        for i in range(len(m)):
            fila.append(m[i][j])   # Agregar el valor de la celda (i,j) a la nueva fila
        resultado.append(fila)
    return resultado

m = []
f = int(input("Ingrese el número de filas de la matriz:    "))  # Ingreso del usuario
c = int(input("Ingrese el número de columnas de la matriz: "))

for i in range(f):
    fila = []
    for j in range(c):
        valor = int(input(f"Ingrese el valor en la posición ({i}, {j}): "))
        fila.append(valor)
    m.append(fila)

print("Matriz ingresada:")   # Imprimir matriz ingresada
for fila in m:
    print(fila)

resultadoTranspuesta = matrizTranspuesta(m)  # Calcular matriz transpuesta
print("Matriz transpuesta:")              # Imprimir la matriz transpuesta
for fila in resultadoTranspuesta:
    print(fila)