from adapter import adapter

import numpy as np


class ProgramGenerate:
    def __init__(self):
        self.matrix_a = []
        self.matrix_b = []

    def generate_matrix_a(self, m, n):
        self.matrix_a = np.random.rand(m, n)
        return self.matrix_a

    def generate_matrix_b(self, m, n):
        self.matrix_b = np.random.rand(m, n)
        return self.matrix_b

    def write_sum_matrix_to_file(self, filename):
        with open(filename, 'w') as file:
            # Сложение матриц А и В
            result_matrix = self.matrix_a + self.matrix_b
            for row in result_matrix:
                file.write(' '.join(str(element) for element in row))
                file.write('\n')


def main_gen():
    # Размерности матриц
    m = 3
    n = 4
    generator = ProgramGenerate()
    generator.generate_matrix_a(m, n)
    generator.generate_matrix_b(m, n)
    file_path = 'F2'
    # Запись матриц A и B в файл F2
    generator.write_sum_matrix_to_file(file_path)
    adapter(file_path)


if __name__ == '__main__':
    main_gen()
