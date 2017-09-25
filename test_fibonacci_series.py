import unittest

from fibonacci_series import generate_fibonacci_series

class FibonacciSeriesTest(unittest.TestCase):
    
    def test_fibonacci_nth_term_is_positive(self):
        self.assertRaises(ValueError, generate_fibonacci_series, -2)
    
    def test_fibonacci_returns_list_with_0(self):
        self.assertListEqual(generate_fibonacci_series(1), [0])
    
    def test_fibonacci_returns_correct_list(self):
        self.assertListEqual(generate_fibonacci_series(3), ['0', '1', '1'])
        self.assertListEqual(generate_fibonacci_series(10), 
                              ['0' , '1' , '1' , '2' , '3' , '5' , '8' , '13' , '21' , '34'])
    
    def test_fibonacci_returns_error_if_nth_term_is_not_number(self):
        self.assertRaises(ValueError, generate_fibonacci_series, 'Ten')

