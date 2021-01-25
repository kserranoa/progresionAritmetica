import sys
import time
import archivo

for n in range (1,10000):
    print(archivo.algoritmo2(n))
    timeAl2 = (time.time())
    print(timeAl2)

#print(sys.getsizeof(archivo.algoritmo2()))

    print(archivo.algoritmo1(n))
    timeAl1 = (time.time())
    print(timeAl1)

    if timeAl1 < timeAl2:
        print("Algoritmo 1 es mejor")
    elif timeAl2 < timeAl1:
        print("Algoritmo 2 es mejor")
