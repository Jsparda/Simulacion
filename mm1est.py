from math import log
import random

velArribo = 3.0
velPartida = 5.0
totalClientes = 1000

ilam = 1/velArribo
imiu = 1/velPartida

arribo = []
previo = 0.0

inicioServicio = []

finServicio = []
salida = 0.0

permanencia = []
suma = 0.0

error = 0.1
confianza = 0.95

media = 0
varianza = 0

for i in range(totalClientes):
    inter = -1 * ilam * log(random.random())
    arribo.insert(i%2,previo+inter)
    previo = arribo[i%2]
    inicioServicio.insert(i%2,max(previo,arribo[i%2]))
    serv = -1 * imiu * log(random.random())
    finServicio.insert(i%2,inicioServicio[i%2] + serv)
    salida = finServicio[i%2]
    permanencia.insert(i%2,finServicio[i%2]-arribo[i%2])
    suma = suma + permanencia[i%2]
    if(i==0):
        media = 0
    elif(i==1):
        varianza = 0
        mediaAnt=media
        media = media + ((salida-media)/i)
    elif(i>1):
        mediaAnt=media
        media = media + ((salida-media)/i)
        varianza = (1-(1/i))*varianza + (i + 1)*(media-mediaAnt)**2


    #######################Sección de prints
    #print("Cliente: %2d" % (i))
    #print("arribo: %6.3f" %(arribo[i%2]))
    #print("inicia: %6.3f" %(inicioServicio[i%2]))
    #print("Termina: %6.3f" %(finServicio[i%2]))
    #print("Permanencia: %6.3f" % permanencia[i%2])
    print("l media es: %6.3f"%media)
    print("===================================")
    print("l varianza es: %6.3f"%varianza)
print("Tiempo promedio en el sistema es: ", suma/totalClientes)
