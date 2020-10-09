import numpy as np
import math

def fact(x=None):
    if(x == 0):
        return 1
    else:
        return (x*fact(x-1))

def probPoisson(lambd,evento):
    valor = 0.0
    contador = 0
    for i in range (evento + 1):
        valor = (((math.e)**(-lambd))*lambd**(i))/fact(i)
        contador = contador + valor
        #print("i=",i,"p(i) =" , valor)
    return valor

H0 = 0.05
lambd = 0.0
proNueva = 0.0


muestras = []
frecuencia = {}
liPro= []
frecuenciaEsp = []

f = open("muestras.txt","r")

for i in f:
    muestras.append(int(i))
maximo = max(muestras)

for j in range(maximo+1):
    frecuencia[j] = muestras.count(j)

for j in range(len(frecuencia)):
    lambd = lambd + (j*(frecuencia[j]))

lambd = (lambd)/len(muestras)
print("Lambda =",lambd)


print("Calculo probabilidades")
for j in range(len(muestras)):   ##Calcula las probabilidades de la lista de muestras
        liPro.append(probPoisson(lambd,muestras[j]))
print(len(liPro))

print("Busco repetidos")
a = [liPro[j] for j in range(len(liPro)) if j == liPro.index(liPro[j])] ##Busca probabilidades repetidas
print("Arroje repetidos")

print("#repetidos:",len(a))
print("#Frecuencias:",len(frecuencia))

del frecuencia["9"]
print("#Frecuencias:",len(frecuencia))

j = 0
for j in range(len(a)):
    frec = len(muestras)*a[j]
    frecuenciaEsp.append(frec)
#print(frecuencia)
#print(frecuenciaEsp)
