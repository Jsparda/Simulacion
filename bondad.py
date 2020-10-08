# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:57:10 2020

@author: Jordan

"""


import numpy as np

cont0 = 0
cont1 = 0
cont2 = 0
contM = 0

lambd = 0

lista = []
frecuencia = []
datos = []

x = open("muestras.txt","r")

for i in x:
    lista.append(int(i))
print (lista)

for j in lista:
    frecuencia.append(lista.count(j))
    
print(frecuencia)
    
        
print("Los contadores respectivos son c0=",cont0,"c1=",cont1,"c2=",cont2,"cM=",contM)
#lambd = (0*cont0 + 1*cont1 + 2*cont2 + 3*contM)/len(lista)
print("La media es lambd=",lambd)
#datos = np.random.poisson(lambd,5000)
#print(datos)
#print(len(datos))