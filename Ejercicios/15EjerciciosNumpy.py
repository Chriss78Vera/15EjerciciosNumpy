import numpy as np
#Ejercicio 1
print("Ejercicio 1") # 5 vector de tamaño 10, el quinto valor =1
Z = np.zeros(10) 
Z[4] = 1
print(Z)
#Ejercicio 2
print("Ejercicio 2")
Z = np.arange(10,50) #6 vector con valores  del 10 al 49
print(Z)
#Ejericio 3
print("Ejercicio 3")
Z = np.arange(10,50) #7 vector invertido
Z = Z[::-1]
print (Z)
#Ejericio 4
print("Ejercicio 4")
Z = np.arange(9).reshape(3,3) #8 matriz de 3x3 con valores del 0-8
print(Z)
#Ejercicio 5
print("Ejercicio 5") #9. muestra los indices del vector que son distintos de 0
nz = np.nonzero([1,2,0,0,4,0])
print(nz)
#Ejercicio 6
print("Ejercicio 6")
Z = np.random.random((10,10)) #12 10 Vector de 10 valores,  con valores aleatorios
print(Z)
Zmin, Zmax = Z.min(), Z.max() # muestra valor min y max
print("Numero min= " + str(Zmin)+", Numero max= "+ str(Zmax))
#Ejercicio 7
print("Ejercicio 7")
Z = np.random.random(5) #13 vector de tam=5
print(Z)
m = Z.mean() #calcula el promedio de todos los valores
print(m)
#Ejercicio 8
print("Ejercicio 8")
Z = np.ones((10,10)) # 14 Matriz de 10x10 los bordes se rellenan de 1
Z[1:9,1:-1] = 0 # Se llenan con ceros [valores de filas, valores de columnas]
print(Z)
#Ejercicio 9
print("Ejercicio 9")
Z = np.diag(3+np.arange(7),k=0) # 16 matriz de 5x5 valores del 3 , arrange(num de matriz cuadrada)-(k es quien define el lugar de la diagonal)
print(Z)
#Ejercicio 10
print("Ejercicio 10")
Z = np.zeros((8,8),dtype=int) # 17 matriz de 8x8 valores enteros patron de juego de ajedrez
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)
#Ejercicio 11
print("Ejercicio 11")
print(np.unravel_index(100,(6,7,8))) # 18 matriz de formas (6,7,8)   índice (x, y, z) del centésimo elemento
#Ejercicio 12
print("Ejercicio 12")
import numpy as np
Z = np.tile( np.array([[0,2],[1,0]]), (100,100))
# 19 matriz   patron de filas , cantidad de filas y columnas con dicho partron
print(Z)
#Ejercicio 13
print("Ejercicio 13")
Z = np.random.random((5,5)) 
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)
#Ejercicio 14
print("Ejercicio 14")
# 23  Dada una matriz 1D, niegue todos los elementos
# que estén entre 3 y 8, en su lugar
Z = np.arange(11)
print(Z)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)
#Ejercicio 15
print("Ejercicio 15")
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))