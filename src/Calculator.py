from src.Subtraction import Subtraction
from Calculator.Addition import

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = addition(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = subtraction(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = multiplication(x, y)
        return self.result

    def divide(self, x, y):
        self.result = division(x, y)
        return self.result

    def square(self, x):
        self.result = square(x)
        return self.result

    def square_root(self, x):
        self.result = square_root(x)
        return self.result

