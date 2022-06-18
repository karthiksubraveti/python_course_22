from calculatorservice import calculatorfunction
import unittest

class CalculatorTest(unittest.TestCase):
    def testAdd(self):
        self.assertTrue(calculatorfunction(10, 10, '+') == 20)

    def testSub(self):
        self.assertTrue(calculatorfunction(10, 10, '-') == 0)

    def testMul(self):
        self.assertTrue(calculatorfunction(10, 10, '*') == 100)

    def testDiv(self):
        self.assertTrue(calculatorfunction(10, 10, '/') == 1)

unittest.main()
