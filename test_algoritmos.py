import unittest
import algoritmos

class TestUtils(unittest.TestCase):
    #pruebas para el algortimo bubble sort
    def test_bubble_sort(self):
        self.assertEqual(algoritmos.bubble_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(algoritmos.bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(algoritmos.bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_insertion_sort(self):
        self.assertEqual(algoritmos.insertion_sort([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(algoritmos.insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(algoritmos.insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_counting_sort(self):
        self.assertEqual(algoritmos.counting_sort([5, 2, 8, 1, 9],9), [1, 2, 5, 8, 9])
        self.assertEqual(algoritmos.counting_sort([1, 2, 3, 4, 5],5), [1, 2, 3, 4, 5])
        self.assertEqual(algoritmos.counting_sort([5, 4, 3, 2, 1],5), [1, 2, 3, 4, 5])
    
    def test_merge_sort(self):
        self.assertEqual(algoritmos.call_merge_sort([1]), [1])
        self.assertEqual(algoritmos.call_merge_sort([3,1,2]), [1, 2, 3])
        self.assertEqual(algoritmos.call_merge_sort([3,1,2,5]), [1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()