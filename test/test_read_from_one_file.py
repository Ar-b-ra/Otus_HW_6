import unittest
import numpy as np

from program_sum import ProgramSum


class YourClassTestCase(unittest.TestCase):
    def setUp(self):
        self.your_object = ProgramSum()

    def test_read_matrix_from_file(self):
        matrix_a, matrix_b = self.your_object.read_matrix_from_file('F1')
        self.assertEqual(matrix_a.tolist(), [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]])
        self.assertEqual(matrix_b.tolist(),
                         [[13.0, 14.0, 15.0, 16.0], [17.0, 18.0, 19.0, 20.0], [21.0, 22.0, 23.0, 24.0]])


if __name__ == '__main__':
    unittest.main()
