# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:20:47 2020

@author: Jordan
"""

def fact(num=None):
    if(num == 0):
        return 1
    else:
        return (num*fact(num-1))
    
def coefBin(n,i):
    numerador = fact(n)
    denominador = fact(i) * fact(n-i)
    
    return (numerador/denominador)
    

def probNext(p,n):
    print("p= ",p)
    print("n= ",n)
    q = 1 - p
    print("q= ",q)
    valor=0
    print("")
    for i in range (n):
        #print(i)
        cof=coefBin(n,i)
        #print("coeficienteBin: ",cof)
        #print(cof)
        pee = p**i
        #print("prob^i: ",pee)
        #print(pee)
        quu = q**(n-i)
        #print("comple^n-i: ",quu)
        #print(quu)
        #valor = coefBin(n,i)*(p**i)*(q**(n-i))
        #print("i=",i,"p(i)=",valor)
        valor = cof*pee*quu
        print(valor)
        
        
print("Dame un valor para n")
n = int(input())
print("Dame un valor para p")
p = float(input())

#print(fact(n))
#print(coefBin(n,p))
probNext(p,n)