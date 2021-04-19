import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEquals(calculator.result, 4)

    def test_addition_calculator(self):
        td_add = CsvReader('src/Addition.csv').data
        for row in td_add:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction_calculator(self):
        td_sub = CsvReader('src/Subtraction.csv').data
        for row in td_sub:
            self.assertNotEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertNotEqual(self.calculator.result, int(row['Result']))

    def test_multiplication_calculator(self):
        td_mul = CsvReader('src/Multiplication.csv').data
        for row in td_mul:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_calculator(self):
        td_div = CsvReader('src/Division.csv').data
        for row in td_div:
            self.assertNotEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
            self.assertNotEqual(self.calculator.result, float(row['Result']))

    def test_square_calculator(self):
        td_sq = CsvReader('src/Square.csv').data
        for row in td_sq:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_root_calculator(self):
        td_sqrt = CsvReader('src/Square Root.csv').data
        for row in td_sqrt:
            self.assertEqual(self.calculator.square_root(float(row['Value 1'])), round(float(row['Result']), 7))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 7))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__=='__main__':
     unittest.main()
