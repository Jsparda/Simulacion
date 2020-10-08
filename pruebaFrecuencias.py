for j in lista:
    if(lista[j] == 0):
        cont0 = cont0 + 1
    elif(lista[j] == 1):
        cont1 = cont1 + 1
    elif(lista[j] == 2):
        cont2 = cont2 + 1
    elif(lista[j] == 3):
        cont1 = cont1 + 1
    elif(lista[j] == 4):
        cont4 = cont4 + 1
    elif(lista[j] == 5):
        cont5 = cont5 + 1
    elif(lista[j] == 6):
        cont6 = cont6 + 1
    elif(lista[j] == 7):
        cont7 = cont7 + 1
    elif(lista[j] == 8):
        cont8 = cont8 + 1
    elif(lista[j] == 9):
        cont9 = cont9 + 1
    elif(lista[j] == 10):
        cont10 = cont10 + 1    
        
print("Los contadores respectivos son c0=",cont0,"c1=",cont1,"c2=",cont2,"c3=",cont3,
      "c4=",cont4,"c5=",cont5,"c6=",cont6,"c7=",cont7,"c8=",cont8,"c9=",cont9,"c10=",cont10)

lambd = (0*cont0 + 1*cont1 + 2*cont2 + 3*cont3+ 4*cont4 + 5*cont5 + 6*cont6 + 7*cont7 +
         8*cont8 + 9*cont9 + 10*cont10)/len(lista)
