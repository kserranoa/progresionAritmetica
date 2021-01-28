prod = [['arroz', 1500, 1], ['lechuga', 500, 3], ['tomate', 1000, 3]]
for x in prod:
    total = x[2] * x[1]
    print("Productos: %s Precio: %i Cantidad: %i Total: %i"\
      %(x[0], x[1], x[2], total))
