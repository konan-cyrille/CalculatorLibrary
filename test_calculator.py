"""
    test unitaire de la librairie Calculatrice
"""


import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def tes_substraction(self):
        assert 2 == calculator.substract(4, 2)
