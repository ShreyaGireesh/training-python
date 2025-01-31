import unittest
from calculator import Calculator  

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()  
        result = calc.add(2, 3)  
        self.assertEqual(result, 5)  

if __name__ == '__main__':
    unittest.main()  
