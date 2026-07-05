import unittest

from calculadora import soma, subtracao, multiplicacao, divisao


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 2), 3)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(4, 3), 12)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(1, 0)


if __name__ == "__main__":
    unittest.main()
