from factorial import fact
import unittest

if __name__ == '__main__':
    class TestFactorial(unittest.TestCase):
        def test_n(self):
            self.assertEqual(fact(5), 120)
        def test_ValueError(self):
            with self.assertRaises(ValueError):
                fact(-1)
        def test_TypeError(self):
            with self.assertRaises(TypeError):
                fact(0.5)


unittest.main()
