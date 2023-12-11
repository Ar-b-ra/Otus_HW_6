import unittest
import numpy as np

from program_generate import ProgramGenerate


class TestGenerateMatrixB(unittest.TestCase):
    def setUp(self):
        self.obj = ProgramGenerate()  # Replace with the name of your class

    def test_generate_matrix_a(self):
        # Testing if the shape of the generated matrix is correct
        m = 3
        n = 4
        result = self.obj.generate_matrix_a(m, n)
        self.assertEqual(result.shape, (m, n))

        # Testing if all elements in the generated matrix are between 0 and 1
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))

    def test_generate_matrix_b(self):
        # Testing if the shape of the generated matrix is correct
        m = 3
        n = 4
        result = self.obj.generate_matrix_b(m, n)
        self.assertEqual(result.shape, (m, n))

        # Testing if all elements in the generated matrix are between 0 and 1
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1))


if __name__ == '__main__':
    unittest.main()
