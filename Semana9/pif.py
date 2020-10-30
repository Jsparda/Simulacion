# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:14:19 2020

@author: Jordan
"""

import sys
from event import Event
from model import Model
from simulation import Simulation

import random

class Algorithm2(Model):
    
    def init(self):
        self.visited = False
        self.rand = round(random.uniform(0.0,10.0),5)
        self.father = self.id
        self.count = 1
        self.mayor = (self.id, self.rand)
        print("Nodo "+str(self.id)+": Inicializo algoritmo\n","\tVecinos =",self.neighbors,"\n","\tNúmero Generado:",self.rand)
        
    def receive(self,event):
        self.count -= 1
        if tupla[1] > self.mayor[1]:
            self.mayor = tupla
        if self.visited == False:
            #print("Recibí mensaje")
            self.visited = True
            self.father = event.source
            for t in (self.neighbors):
                if t - (self.father) != 0:
                    newevent = Event((-1,-1),self.clock+1.0, t, self.id)
                    self.transmit(newevent)
                    self.count += 1
        if self.count == 0:
            if self.father != self.id:
                print("Nodo "+str(self.id)+": Terminó el algortimo\n","\tPadre = ",self.father)
                newevent = Event(self.mayor,self.clock+1.0,self.father,self.id)
                self.transmit(newevent)
            else:
                print("El número más grande es:",self.mayor)
                
                
            
#Función de inicio
if len(sys.argv) != 2:
    print("Por favor proporciona un nombre de archivo")
    raise SystemExit(1)
experiment = Simulation(sys.argv[1],500)
#Asocia una pareja proceso/modelo con cada nodo de la gráfica
for i in range(1,len(experiment.graph)+1):
    m = Algorithm2()
    experiment.setModel(m,i)
#Inserta un evento semilla en la agenda y arranca
tupla =(-1,-1)
seed = Event(tupla,0.0,1,1)
experiment.init(seed)
experiment.run()
