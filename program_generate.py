from adapter import adapter

import numpy as np


# Генерация матрицы A размером m x n
def generate_matrix_A(m, n):
    return np.random.rand(m, n)


# Генерация матрицы B размером n x p
def generate_matrix_B(n, p):
    return np.random.rand(n, p)


# Запись матрицы в файл
def write_matrix_to_file(matrix, filename):
    with open(filename, 'a') as file:
        for row in matrix:
            file.write(' '.join(str(element) for element in row))
            file.write('\n')


def main_gen():
    # Размерности матриц
    m = 3
    n = 4

    # Генерация матриц A и B
    matrix_A = generate_matrix_A(m, n)
    matrix_B = generate_matrix_B(m, n)
    file_path = 'F2'
    # Запись матриц A и B в файл F2
    write_matrix_to_file(matrix_A, file_path)
    write_matrix_to_file(matrix_B, file_path)
    adapter(file_path)


if __name__ == '__main__':
    main_gen()
