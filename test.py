import math
import random
import matplotlib.pyplot as plt

puntosTotales = 1000
puntosDentro = 0
conspi = 0

vector = []

while(len(vector) < 50):
    puntosDentro = 0
    for i in range (puntosTotales):
        coordx=random.random()
        coordy=random.random()
        tiro = math.sqrt((coordx**2)+(coordy**2))
        if(tiro < 1):
            puntosDentro = puntosDentro + 1
    conspi = 4 * (puntosDentro/puntosTotales)
    vector.append(conspi)
print(vector)
print("=============================================")
plt.hist(vector, 20, edgecolor='white', linewidth=1)
plt.ylabel('Frecuecia')
plt.xlabel('Valores')
plt.title('Histograma')
plt.show()