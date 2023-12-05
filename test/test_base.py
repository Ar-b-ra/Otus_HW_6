import unittest
from unittest.mock import patch

from program_generate import main_gen


class TestMainGen(unittest.TestCase):
    @patch('builtins.input', side_effect=[3, 4])
    @patch('program_generate.generate_matrix_A', return_value=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    @patch('program_generate.generate_matrix_B', return_value=[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])
    @patch("program_sum.read_matrix_from_file", return_value=([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                                                              [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]))
    @patch('program_generate.write_matrix_to_file')
    @patch('adapter.adapter')
    def test_main_gen(self, mock_adapter, mock_write_matrix_to_file, mock_read_matrix_from_file, mock_generate_matrix_B,
                      mock_generate_matrix_A,
                      mock_input):
        main_gen()
        mock_generate_matrix_A.assert_called_once_with(3, 4)
        mock_generate_matrix_B.assert_called_once_with(3, 4)
        mock_write_matrix_to_file.assert_any_call([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 'F2')
        mock_write_matrix_to_file.assert_any_call([[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]], 'F2')


if __name__ == '__main__':
    unittest.main()
