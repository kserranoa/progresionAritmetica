prod = [['arroz', 1500, 1], ['lechuga', 500, 3], ['tomate', 1000, 3]]

#print([i*3 for i in prod])

#print(prod[0+1][0])
letras = ['a', 'b', 'c', 'a']
if 'a' in letras:
    print("i")
    
#Saber cuantas veces
print(letras.count('a'))

#Reverse
letras.reverse()
print(letras)

#Acceder elementos en orden contrario
so = ['Windows', 'MacOs', 'Linux']
for o in reversed(so):
    print(o)
