import sys
import time
import archivo
import factorial
import Suma
import Division

datos = [0, 1, 3.0, "hola", -4, 20000000, 1000000000]
'''for x in datos:
    for x1 in datos:
        print(Suma.suma(x, x1))
'''
for x in range(0, len(datos)):
    for x1 in range(0, len(datos)):
        print(Division.division(datos[x], datos[x1]))
