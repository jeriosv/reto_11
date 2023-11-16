# Reto No. 11: Matrices.

## Una matriz es un arreglo rectangular de elementos del mismo tipo, esto es una colección de n x m arreglos.

## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```


## 2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

## 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

## 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python
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
```

## 5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.

```python
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
```
