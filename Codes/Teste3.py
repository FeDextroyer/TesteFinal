import unittest
from flask import Flask

app = Flask(__name__)

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x // y  # Retorna divisão inteira

# Testes unitários
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(5, 3), 8)
        self.assertEqual(Calculator.add(-5, 3), -2)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        self.assertEqual(Calculator.subtract(-5, 3), -8)
        self.assertEqual(Calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(5, 3), 15)
        self.assertEqual(Calculator.multiply(-5, 3), -15)
        self.assertEqual(Calculator.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(-10, 2), -5)
        self.assertEqual(Calculator.divide(10, -2), -5)
        self.assertEqual(Calculator.divide(-10, -2), 5)
        self.assertEqual(Calculator.divide(0, 5), 0)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
