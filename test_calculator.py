import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) #actual output vs expected output

    # Add the following test methods to the TestCalculator class:

    #case add
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1,-2),-3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1,0),1)

    #case subtract
    def test_sub(self):
        self.assertEqual(self.calc.subtract(-2,1),-3)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(1,-4),5)

    #case multiply
    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(-2,2),-4)

    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(2,0),0)

    #case divide
    def test_divide_aEqualb(self):
        self.assertEqual(self.calc.divide(2,2),1)

    def test_divide_By_zero(self):
        self.assertEqual(self.calc.divide(4,0),"error")

    #case modulo
    def test_mod(self):
        self.assertEqual(self.calc.modulo(7,3),1)

    def test_mod_resultZero(self):
        self.assertEqual(self.calc.modulo(6,3),0)

   

if __name__ == '__main__':
    unittest.main()