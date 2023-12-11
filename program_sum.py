import numpy as np


class ProgramSum:

    def __init__(self):
        self.matrix_a = []
        self.matrix_b = []

    # Чтение матрицы из файла
    def read_matrix_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            matrix = []
            for line in lines:
                row = [float(element) for element in line.split()]
                matrix.append(row)
            self.matrix_a = np.array(matrix[:len(matrix) // 2])
            self.matrix_b = np.array(matrix[len(matrix) // 2:])
            return self.matrix_a, self.matrix_b

    # Сложение матриц
    def add_matrices(self):
        return self.matrix_a + self.matrix_b

    # Запись матрицы в файл
    def write_sum_matrix_to_file(self, filename):
        with open(filename, 'w') as file:
            matrix = self.add_matrices()
            for row in matrix:
                file.write(' '.join(str(element) for element in row))
                file.write('\n')


def main_sum(file_path="F0"):
    summer = ProgramSum()

    # Чтение матриц А и В из файла F0
    summer.read_matrix_from_file(file_path)

    # Запись суммы результата в файл F1
    summer.write_sum_matrix_to_file("F1")

    print(f"Результат А+В успешно записан в файл F1.")
