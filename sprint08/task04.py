import unittest
from math import sqrt


class TriangleNotValidArgumentException(Exception):
    def __init__(self):
        self.data = "Not valid arguments"
        super().__init__(self.data)

    def str(self):
        return repr(self.data)


class TriangleNotExistException(Exception):
    def __init__(self):
        self.data = "Can`t create triangle with this arguments"
        super().__init__(self.data)

    def str(self):
        return repr(self.data)

class Triangle:
    def __init__(self, size_list):
        if type(size_list) == tuple and len(size_list) == 3:
            self.size_list = size_list
        else:
            raise TriangleNotValidArgumentException()

        a = self.size_list[0]
        b = self.size_list[1]
        c = self.size_list[2]

        if type(a) == str or type(b) == str or type(c) == str:
            raise TriangleNotValidArgumentException()

        if a + b <= c or a + c <= b or c + b <= a or (a < 0 or b < 0 or c < 0):
            raise TriangleNotExistException()

    def get_area(self):
        a = self.size_list[0]
        b = self.size_list[1]
        c = self.size_list[2]

        p = sum(self.size_list) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


class TriangleTest(unittest.TestCase):
    def test_valid(self):
        actual = Triangle((3, 4, 5))
        self.assertEqual(actual.get_area(), 6.0)

    def test_not_valid(self):
        with self.subTest():
            self.assertRaises(TriangleNotExistException, Triangle, (1, 2, 3))

    def test_not_valid_arguments(self):
        with self.subTest():
            self.assertRaises(TriangleNotValidArgumentException, Triangle, (1, 2, '3'))
