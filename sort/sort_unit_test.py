"""UnitTest for Sorting Algorithms"""
from random import randint, seed
import unittest
import sort


class SortTester(unittest.TestCase):
    """Sorting Tester Class"""

    @classmethod
    def setUpClass(cls):
        """Initalize Test Cases for sorting."""
        seed(1)
        positive_increasing = [v for v in range(10)]
        positive_decreasing = [v for v in range(10, 0, -1)]
        random_positive = [randint(0, 100) for _ in range(10)]
        negative_decreasing = [v for v in range(0, -10, -1)]
        negative_increasing = [v for v in range(-10, 0)]
        random_negative = [randint(-100, 0) for _ in range(10)]
        random_total = [randint(-100, 100) for _ in range(10)]
        cls.test_cases = [positive_increasing, positive_decreasing,
                          random_positive, negative_decreasing,
                          negative_increasing, random_negative, random_total]

    def test_bubble_sort(self):
        """Testing Bubble Sort Function."""
        print('Testing Ascending Sort')
        print('-'*100)
        for case in self.test_cases:
            print(f'Unsorted Array: {case}')
            sorted_case = sort.bubble_sort(case)
            print(f'Sorted Array {sorted_case}')
            self.assertEqual(sorted(case), sorted_case)

        print('-'*100)
        print('Testing Decending Sort')
        for case in self.test_cases:
            print(f'Unsorted Array: {case}')
            sorted_case = sort.bubble_sort(case, reverse=True)
            print(f'Sorted Array {sorted_case}')
            self.assertEqual(sorted(case, reverse=True), sorted_case)
        print('-'*100)

    def test_insertion_sort(self):
        """Testing Insertion Sort"""
        print("Testing Ascending Sort")
        print('-'*100)
        for case in self.test_cases:
            print(f'Unsorted Array: {case}')
            sorted_case = sort.insertion_sort(case)
            print(f'Sorted Array {sorted_case}')
            self.assertEqual(sorted(case), sorted_case)

        print('-'*100)
        print("Testing Decending Sort")
        for case in self.test_cases:
            print(f'Unsorted Array: {case}')
            sorted_case = sort.insertion_sort(case, reverse=True)
            print(f'Sorted Array {sorted_case}')
            self.assertEqual(sorted(case, reverse=True), sorted_case)
        print('-'*100)


if __name__ == '__main__':
    unittest.main()
