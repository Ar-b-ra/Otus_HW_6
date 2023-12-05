import numpy as np


# Чтение матрицы из файла
def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = [float(element) for element in line.split()]
            matrix.append(row)
        return np.array(matrix[:len(matrix) // 2]), np.array(matrix[len(matrix) // 2:])


# Сложение матриц
def add_matrices(matrix_A, matrix_B):
    return matrix_A + matrix_B


# Запись матрицы в файл
def write_matrix_to_file(matrix, filename):
    with open(filename, 'w') as file:
        for row in matrix:
            file.write(' '.join(str(element) for element in row))
            file.write('\n')


def main_sum(file_path="F0"):
    # Чтение матриц А и В из файла F0
    matrix_A, matrix_B = read_matrix_from_file(file_path)

    # Сложение матриц А и В
    result_matrix = add_matrices(matrix_A, matrix_B)

    # Запись результата в файл F1
    write_matrix_to_file(result_matrix, "F1")

    print(f"Результат А+В успешно записан в файл F1.")
