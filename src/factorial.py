"""Módulo que contiene la funcion factorial"""
def factorial(n):
    """
    Función para cálcular el factorial de un número

    
    Entrada:
    - entero: número entero al que cálcular el factorial
    
    
    Salida:
    - entero: número entero resultado de cálcular el factorial   
    
    """
    if not isinstance(n,int):
        raise TypeError("Solo se aceptan enteros")
    if n<0:
        raise ValueError("Los números negativos no son validos")
    if n == 1:
        return 1
    return n*factorial(n-1)
