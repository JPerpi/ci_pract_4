import pytest
from src.factorial import *

def test_factorial_1():
    assert factorial(1)==1

def test_factorial_de_5_es_120():
    assert factorial(5) == 120

def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_no_int():
    with pytest.raises(TypeError):
        factorial('hola')