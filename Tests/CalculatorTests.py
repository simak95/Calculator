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

    def test_subtraction(self):
        test_data = CsvReader("src/Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__=='__main__':
     unittest.main()
