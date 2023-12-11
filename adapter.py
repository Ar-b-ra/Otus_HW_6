from program_sum import ProgramSum


class Adapter:
    def __init__(self):
        self.adapter = ProgramSum()

    def sum_matrices(self, file_path="F0"):
        self.adapter.read_matrix_from_file(file_path)
        self.adapter.write_sum_matrix_to_file("F1")


