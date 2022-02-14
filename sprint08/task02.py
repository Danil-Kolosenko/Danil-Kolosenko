import unittest

def divide(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivisionError
    return float(num_1) / num_2

class DivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide1(self):
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide2(self):
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_error(self):
        self.assertRaises("error", divide, 10, 0)
