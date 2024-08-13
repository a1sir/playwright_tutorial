import pytest
from refactor_calc_3 import Calc


class TestCalc:

    def test_addition(self):
        calc = Calc()
        assert calc.addition(1, 2) == 3
        assert calc.addition(-1, 3) == 2
        assert calc.addition(-1, -3) == -4

    def test_subtract(self):
        calc = Calc()
        assert calc.subtract(1, 2) == -1
        assert calc.subtract(-1, 3) == -4
        assert calc.subtract(-1, -3) == 2

    def test_multiplication(self):
        calc = Calc()
        assert calc.multiplication(2, 2) == 4
        assert calc.multiplication(2, 0) == 0
        assert calc.multiplication(-5, 2) == -10

    def test_division(self):
        calc = Calc()
        assert calc.division(100, 10) == 10
        assert calc.division(256, 8) == 32
        assert calc.division(-10, 2) == -5

    def test_exponentiation(self):
        calc = Calc()
        assert calc.exponentiation(2, 2) == 4
        assert calc.exponentiation(2, 32) == 4294967296
        assert calc.exponentiation(-10, 3) == -1000

    def test_remainder(self):
        calc = Calc()
        assert calc.remainder(10, 3) == 1
        assert calc.remainder(100, 30) == 10
        assert calc.remainder(-1000, 100) == 0

    def test_calculate(self):
        calc = Calc()
        assert calc.calculate(2, 3, '+') == 5
        assert calc.calculate(5, 3, '-') == 2
        assert calc.calculate(10, 2, '*') == 20
        assert calc.calculate(10, 2, '**') == 100
        assert calc.calculate(5, 2, '%') == 1
