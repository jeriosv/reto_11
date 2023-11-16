def ingresarMatriz(nombre):    #Función que lee los datos de la matriz
    matriz = []
    f = int(input(f"Ingrese el número de filas de la matriz No. {nombre}:    "))
    c = int(input(f"Ingrese el número de columnas de la matriz No. {nombre}: "))
    for i in range(f):
        fila = []
        for j in range(c):
            valor = int(input(f"Ingrese el valor de la matriz No. {nombre} en la posición ({i}, {j}) : "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumarMatrices(m1, m2):    # Función que suma dos matrices
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

def restarMatrices(m1, m2):   # Función que resta dos matrices
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    return resultado

m1 = ingresarMatriz("1")      # Ingreso del usuario de las 2 matrices
m2 = ingresarMatriz("2")

print("Matriz 1:")            # Imprimir matriz 1
for fila in m1:
    print(fila)

print("Matriz 2:")            # Imprimir matriz 2
for fila in m2:
    print(fila)


if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):    # Verificar el tamaño de las matrices
    print("Las matrices no tienen el mismo tamaño. No se pueden sumar.")
else:
    resultadoSuma = sumarMatrices(m1, m2)                 # Sumar matrices
    print("El resultado de la suma de las matrices es:")  # Imprimir la suma
    for fila in resultadoSuma:
        print(fila)
    
    resultadoResta = restarMatrices(m1, m2)                # Restar matrices
    print("El resultado de la resta de las matrices es:")  # Imprimir la resta
    for fila in resultadoResta:
        print(fila)