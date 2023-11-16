def sumarFila(matriz, fila):    # Función para sumar los elementos de una fila dada de una matriz
    if fila < 0 or fila >= len(matriz):    # Verificar que la fila sea válida
        print("La fila ingresada no es válida.")
        return None
    suma = 0
    for elemento in matriz[fila]:    # Sumar los elementos de la fila
        suma += elemento
    return suma

matriz = []
filas =    int(input("Ingrese el número de filas de la matriz:    "))  # Ingreso del usuario
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

# Ingreso del usuario de la fila a sumar
fila = int(input("Ingrese el número de la fila a sumar: (primera 1, segunda 2, ...): "))

resultadoSuma = sumarFila(matriz, fila-1)    # Sumar los elementos de la fila
print("La suma de los elementos de la fila " +  str(fila) + " es: " + str(resultadoSuma))