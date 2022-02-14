import unittest
import math


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("error")


    discriminant = (b**2) - (4*a*c)
    if discriminant > 0 and a != 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2

    elif discriminant == 0 and a != 0:
        x = -b / (2 * a)
        return x

    else:
        return None


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_pos(self):
        self.assertEqual(quadratic_equation(2, 1, -1), (0.5, -1.0))
        self.assertEqual(quadratic_equation(2, -5, -7), (3.5, -1.0))

    def test_discriminant_neg(self):
        self.assertEqual(quadratic_equation(8, 4, 3), None)
        self.assertEqual(quadratic_equation(3, 1, 1), None)

    def test_discriminant_zero(self):
        self.assertEqual(quadratic_equation(3, -18, 27), 3.0)
        self.assertEqual(quadratic_equation(4, -12, 9), 1.5)

    def test_error(self):
        #self.assertEqual(quadratic_equation(0, 0, 0), "error")
        self.assertRaises(ValueError, quadratic_equation, 0, 0, 0)
