# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:42:53 2020

@author: Jordan
"""
import math

def fact(x=None):
    if(x == 0):
        return 1
    else:
        return (x*fact(x-1))
    

def prob(lambd,evento):
    contador = 0
    for i in range (evento + 1):
        #print (i)
        #if(i > 0):
            valor = (((math.e)**(-lambd))*lambd**(i))/fact(i)
            contador = contador + valor
        #valor = math.e**(-lambd) - (indice-i)
        #valor = (indice-i) * fact(indice-i)
        #print("pase ", i ," vez")
            #print("i =", (i) ,"p(x) =", valor)
        #if (i == 0):
         #   valor = 0
            print("i =", (i) ,"p(x) =", valor)
          
    print("")
    print("")
    print("La suma de los P(i<=50) es ",contador)
    print("########")
    print("P(i>40)=",(1-contador))
    

print("Cuanto vale lambda?")
lambd = float(input())
print("Que numero es i?")
evento = int(input())

print("###################################")

prob(lambd,evento)