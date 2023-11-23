from calculadora import Calculadora

def test_somar():
    calc = Calculadora()
    resultado = calc.somar(3, 5)
    assert resultado == 8

def test_subtrair():
    calc = Calculadora()
    resultado = calc.subtrair(8, 3)
    assert resultado == 5

def test_multiplicar():
    calc = Calculadora()
    resultado = calc.multiplicar(4, 6)
    assert resultado == 24

def test_dividir():
    calc = Calculadora()
    resultado = calc.dividir(10, 2)
    assert resultado == 5

    resultado = calc.dividir(7, 3)
    assert resultado == 2.3333

def test_dividir_por_zero():
    calc = Calculadora()
    with pytest.raises(ValueError):
        calc.dividir(5, 0)
