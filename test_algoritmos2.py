import unittest
import algoritmos2

class TestUtils(unittest.TestCase):
    #pruebas para el algortimo selection sort
    def test_selection_sort(self):
        self.assertEqual(algoritmos2.selectionsort([86, 44, 21, 19]), [19, 21, 44, 86])
        self.assertEqual(algoritmos2.selectionsort([67, 55, 28, 49]), [28, 49, 55, 67])

    #pruebas para el algortimo quick sort
    def test_quicksort_sort(self):
        self.assertEqual(algoritmos2.QuickSort([2]), [2])
        self.assertEqual(algoritmos2.QuickSort([12, 4, 23, 1, 7]), [1, 4, 7, 12, 23])

    #pruebas para el algortimo heap sort
    def test_heapsort_sort(self):
        self.assertEqual(algoritmos2.heap_sort([33,35,42,10,7,8,14,19,48]), [7,8,10,14,19,33,35,42,48])
        self.assertEqual(algoritmos2.heap_sort([16, 2, 23, 5, 7]), [2, 5, 7, 16, 23])


if __name__ == '__main__':
    unittest.main()