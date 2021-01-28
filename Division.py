def division(n1, n2):
    try:
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = "No divisor 0"
        return resultado
    except TypeError:
        print("No ingrese texto")
