import unittest
from calculadora import *

class TesteCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(5, adicionar(2, 3))

    def test_multiplicacao(self):
        self.assertEqual(6, multiplicar(2, 3))

    def test_subtrair(self):
        self.assertEqual(5, subtrair(2, 3))

    def test_dividir(self):
        self.assertEqual(6, dividir(2, 3))

    def test_se_tentar_dividir_por_zero_deve_retornar_uma_ValueError(self):
        self.assertRaises(ValueError, dividir(10,0))
        
if __name__ == "__main__":
    unittest.main()