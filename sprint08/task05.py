import unittest

class Worker:
    def __init__(self, name, salary=0.0):
        self.name = name
        self.salary = salary
        self.result = 0.0

    def get_tax_value(self):
        if self.salary == 0.0:
            return self.salary

        elif self.salary < 1000:
            return 0.0

        elif self.salary in range(1001, 3001):
            self.result += 0.1 * (self.salary - 1000)

        elif self.salary in range(3001, 5001):
            self.result += 0.15 * (self.salary - 3000) + 0.1 * (3000 - 1000)

        elif self.salary in range(5001, 10001):
            self.result += 0.21 * (self.salary - 5000) + 0.15 * (5000 - 3000) + 0.1 * (3000 - 1000)

        elif self.salary in range(10001, 20001):
            self.result += 0.30 * (self.salary - 10000) + 0.21 * (10000 - 5000) + 0.15 * (5000 - 3000)\
                           + 0.1 * (3000 - 1000)

        elif self.salary in range(20001, 50001):
            self.result += 0.40 * (self.salary - 20000) + 0.30 * (20000 - 10000)\
                           + 0.21 * (10000 - 5000) + 0.15 * (5000 - 3000) + 0.1 * (3000 - 1000)

        elif self.salary > 50000:
            self.result += 0.47 * (self.salary - 50000) + 0.40 * (50000 - 20000) + 0.30 * (20000 - 10000)\
                           + 0.21 * (10000 - 5000) + 0.15 * (5000 - 3000) + 0.1 * (3000 - 1000)

        return self.result

class WorkerTest(unittest.TestCase):
    def test_test1(self):
        pass

    def test_test2(self):
        pass

    def test_test3(self):
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 2)
