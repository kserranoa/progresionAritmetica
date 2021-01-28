def suma(n1, n2):
    try:
        resultado = n1+n2
        return resultado
    except TypeError:
        print("No ingrese texto")
