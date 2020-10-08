# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:57:10 2020

@author: Jordan

"""

import numpy as np
import math

def fact(x=None):
    if(x == 0):
        return 1
    else:
        return (x*fact(x-1))

def probPoisson(lambd,evento):
    valor = 0
    contador = 0
    for i in range (evento + 1):
        valor = (((math.e)**(-lambd))*lambd**(i))/fact(i)
        contador = contador + valor
        print("i=",i,"p(i) =" , valor)

alpha = 0.05

lambd = 0.0

lista = []
frecuencias = {}

prob = 0.0

f = open("muestras.txt","r")

for i in f:
    lista.append(int(i))
maximo = max(lista)
#print(maximo)

for j in range(maximo+1):
    frecuencias[j] = lista.count(j)

for j in range(len(frecuencias)):
    lambd = lambd + (j*(frecuencias[j]))

lambd = (lambd)/len(lista)

print("lamda =",lambd)

datos = np.random.poisson(lambd,5000)
#print(datos)
#print(len(datos))

######Uso del metodo probPoisson####
j=0
for j in range(len(datos)):
    prob = probPoisson(lambd,datos[j]) ##Revisar!!!!