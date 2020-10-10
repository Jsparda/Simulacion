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
t = 0.0

ti = []
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
## a es la lista de probabilidades repetidas
a = [liPro[j] for j in range(len(liPro)) if j == liPro.index(liPro[j])] ##Busca probabilidades repetidas 
print("Arroje repetidos")

print("#repetidos:",len(a))
print("#Frecuencias:",len(frecuencia))


j = 0
#Frecuencia esperada
for j in range(len(a)):
    frec = len(muestras)*a[j]
    frecuenciaEsp.append(frec)
    
for j in range(len(frecuenciaEsp)):
    tiA = ((frecuencia[j]-frecuenciaEsp[j])**2)/frecuenciaEsp[j]
    ti.append(tiA)
    t = t + ti[j]
print("t=",t,"len ti",len(ti))


print("========================Poisson==================================")
#Genero los valores aleatorios con Poisson



poissA = []
poiss = np.random.poisson(lambd,5000)
poissA = poiss.tolist()

maxPoiss = max(poissA)
print(maxPoiss)

frecuenciaPoiss = {}
freccEspPois = []

j=0
for j in range(maximo+1):
    frecuenciaPoiss[j] = poissA.count(j)
print("FrecuenciaPoiss",len(frecuenciaPoiss))

probPoiss = []

j = 0

for j in range(len(poiss)):
    pro = probPoisson(lambd,poissA[j])
    probPoiss.append(pro)
print(len(probPoiss))

#Frecuencia esperada

j = 0
#Frecuencia esperada
for j in range(len(frecuenciaPoiss)):
    frec2 = len(poissA)*frecuenciaPoiss[j]
    freccEspPois.append(frec2)
print(len(freccEspPois))

ti2 = []
t2 = 0.0
Qr = 0
print("==================Aceptación====================")
for j in range(len(freccEspPois)):
    tiB = ((frecuencia[j]-freccEspPois[j])**2)/freccEspPois[j]
    #print("Ti=",tiB,">= t=",t,"?")
    if(tiB >= t):
        #print("Aumento")
        Qr = Qr + 1
        
gamma = Qr/5000
print("Qr/5000=",gamma)
if(gamma > H0):
    print("aceptado")
else:
    print("rechazo")
    


