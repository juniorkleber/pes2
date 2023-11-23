import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calculadora.somar(3, 5), 8)

    def test_subtrair(self):
        self.assertEqual(self.calculadora.subtrair(8, 3), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calculadora.multiplicar(4, 6), 24)

    def test_dividir(self):
        self.assertEqual(self.calculadora.dividir(10, 2), 5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calculadora.dividir(5, 0)

if __name__ == '__main__':
    unittest.main()
