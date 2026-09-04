import pytest

from calculadora import calcular


def test_sumar():
    assert calcular(5,"+", 3) == 8


def test_restar():
    assert calcular(10,"-", 4) == 6


def test_multiplicar():
    assert calcular(5,"*",  4) == 20


def test_dividir():
    assert calcular(10,"/", 2) == 5


def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        calcular(10,"/", 0)
