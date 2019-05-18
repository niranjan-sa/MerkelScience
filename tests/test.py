import unittest
from src.PositiveElementSearch import positive_elem
from src.MinSliceSumProblem import min_sum_efficient, min_sum


class TestStringMethods(unittest.TestCase):
    """
    This class contains exaustive test suite for the problems one and two and their solutions.
    """

    def test_positive_no(self):
        self.assertEqual(positive_elem([1]), 2)
        self.assertEqual(positive_elem([0]), 1)
        self.assertEqual(positive_elem([-1]), 1)
        self.assertEqual(positive_elem([1, 2, 3]), 4)
        self.assertEqual(positive_elem([-1, -3]), 1)
        self.assertEqual(positive_elem([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(positive_elem([1, 1, 1, 4]), 2)
        self.assertEqual(positive_elem([2, 2, 4, 4]), 1)

    def test_min_sum(self):
        self.assertEqual(min_sum([2, -4, 6, -3, 9]), 1)
        self.assertEqual(min_sum([2]), 2)
        self.assertEqual(min_sum([2, 1]), 1)
        self.assertEqual(min_sum([-1, -1, -10, 10]), 0)
        self.assertEqual(min_sum([10, 10, 10, -30]), 0)

    def test_min_sum_efficient(self):
        self.assertEqual(min_sum_efficient([2, -4, 6, -3, 9]), 1)
        self.assertEqual(min_sum_efficient([2]), 2)
        self.assertEqual(min_sum_efficient([2, 1]), 1)
        self.assertEqual(min_sum_efficient([-1, -1, -10, 10]), 0)
        self.assertEqual(min_sum_efficient([10, 10, 10, -30]), 0)


if __name__ == '__main__':
    unittest.main()