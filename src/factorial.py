def factorial(n):
    if not isinstance(n,int):
        raise TypeError("Solo se aceptan enteros")
    if n<0:
        raise ValueError("Los números negativos no son validos")
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
