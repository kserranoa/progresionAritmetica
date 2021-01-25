def algoritmo1(n):
    repeticion = 0
    total = 0
    while repeticion < n+1:
        total = (total + repeticion)
        repeticion+=1
    return total

def algoritmo2(n):
    total = ((n*(n+1)) / 2)
    return total
