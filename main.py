
import numpy as np


print("")
print("Esta es una multiplicación de Matrices \n")

row1 = int(input("Ingrese el tamaño de la fila: "))
col1 = int(input("Ingrese el tamaño de la comlumna: "))

print("")

arreglo1 = []
for i in range(row1):
    arreglo1.append([])
    for j in range(col1):
        valor = int(input("Ingrese los valores de la Fila {}, Columnna {}: ".format(i + 1, j + 1)))
        arreglo1[i].append(valor)

print("")
matriz1 = np.array(arreglo1)

row2 = int(input("Ingrese el tamaño de la fila: "))
col2 = int(input("Ingrese el tamaño de la comlumna: "))

print("")

arreglo2 = []
for i in range(row2):
    arreglo2.append([])
    for j in range(col2):
        valor = int(input("Ingrese los valores de la Fila {}, Columnna {}: ".format(i + 1, j + 1)))
        arreglo2[i].append(valor)

print("")
matriz2 = np.array(arreglo2)
print("Matriz 1: \n", matriz1)
print("Matriz 2: \n", matriz2)

print("")
print("Resultado de la multiplicación con numpy")

matrizResultante = np.dot(arreglo1, arreglo2)
print(matrizResultante)