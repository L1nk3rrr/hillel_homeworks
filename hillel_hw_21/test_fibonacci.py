import unittest

from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fib = Fibonacci()

    def test_fibonacci_normal_data(self):
        self.assertEqual(self.fib(10), 55)
        self.assertEqual(self.fib(20), 6765)

    def test_large_input(self):
        result = self.fib(111)
        self.assertEqual(result, 70492524767089125814114)

    def test_fibonacci_cache(self):
        self.assertEqual(self.fib.cache, [0, 1])
        self.fib(5)
        self.assertEqual(self.fib.cache, [0, 1, 1, 2, 3, 5])

    def test_empty_values(self):
        with self.assertRaises(TypeError):
            self.fib()

    def test_float(self):
        with self.assertRaises(ValueError):
            self.fib(3.14)

    def test_none(self):
        with self.assertRaises(ValueError):
            self.fib(None)

    def test_string(self):
        with self.assertRaises(ValueError):
            self.fib("string")

    def test_iterable_types(self):
        with self.assertRaises(ValueError):
            self.fib(dict())
        with self.assertRaises(ValueError):
            self.fib(list())
        with self.assertRaises(ValueError):
            self.fib(tuple())
        with self.assertRaises(ValueError):
            self.fib(set())

    def test_bool(self):
        # (True is converted to 1 in this case)
        self.assertEqual(self.fib(True), 1)


if __name__ == '__main__':
    unittest.main()
