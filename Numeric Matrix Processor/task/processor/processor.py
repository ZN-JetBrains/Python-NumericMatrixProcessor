from enum import IntEnum


class Menu(IntEnum):
    EXIT = 0,
    ADD_MATRICES = 1,
    MULTIPLY_MATRIX_CONSTANT = 2,
    MULTIPLY_MATRICES = 3,
    TRANSPOSE_MATRIX = 4


class Transposition(IntEnum):
    MAIN_DIAGONAL = 1,
    SIDE_DIAGONAL = 2,
    VERTICAL_LINE = 3,
    HORIZONTAL_LINE = 4


class Matrix:
    def __init__(self):
        self.matrix_a = []
        self.matrix_b = []
        self.dimensions_a = []
        self.dimensions_b = []

    def reset(self):
        self.matrix_a = []
        self.matrix_b = []
        self.dimensions_a = []
        self.dimensions_b = []

    @staticmethod
    def print_menu():
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("0. Exit")

    @staticmethod
    def print_matrix(a_matrix):
        for row in a_matrix:
            for element in row:
                print(element, end=" ")
            print()

    @staticmethod
    def is_equal_dimensions(dimensions_a, dimensions_b):
        if dimensions_a[0] == dimensions_b[0] and dimensions_a[1] == dimensions_b[1]:
            return True
        return False

    @staticmethod
    def is_matrices_multipliable(dimensions_a, dimensions_b):
        if dimensions_a[1] == dimensions_b[0]:
            return True
        return False

    @staticmethod
    def read_matrix(a_matrix, a_dimensions):
        rows = a_dimensions[0]
        for _ in range(rows):
            new_row = [int(x) if x.isdigit() else float(x) for x in input().split(' ')]
            a_matrix.append(new_row)

    @staticmethod
    def get_dimensions():
        return [int(x) for x in input().split(' ')]

    @staticmethod
    def sum_matrices(a_matrix_a, a_matrix_b):
        return [[x + y for x, y in zip(a, b)] for a, b in zip(a_matrix_a, a_matrix_b)]

    @staticmethod
    def multiply_matrix_constant():
        matrix_size = [int(x) for x in input("Enter size of matrix: ").split(' ')]
        print("Enter matrix: ")
        matrix = []
        Matrix.read_matrix(matrix, matrix_size)
        multiplier_ = float(input("Enter constant: "))
        Matrix.multiply_matrix(matrix, multiplier_)
        print("The result is: ")
        Matrix.print_matrix(matrix)
        print()

    @staticmethod
    def multiply_matrix(a_matrix, a_multiplier):
        for row in a_matrix:
            for index, element in enumerate(row):
                row[index] = element * a_multiplier

    def read_matrices(self):
        print("Enter size of first matrix: ", end="")
        self.dimensions_a = Matrix.get_dimensions()
        print("Enter first matrix:")
        Matrix.read_matrix(self.matrix_a, self.dimensions_a)

        print("Enter size of second matrix: ", end="")
        self.dimensions_b = Matrix.get_dimensions()
        print("Enter second matrix:")
        Matrix.read_matrix(self.matrix_b, self.dimensions_b)

    def add_matrices(self):
        self.read_matrices()

        if Matrix.is_equal_dimensions(self.dimensions_a, self.dimensions_b):
            new_matrix = Matrix.sum_matrices(self.matrix_a, self.matrix_b)
            print("The result is:")
            Matrix.print_matrix(new_matrix)
            print()
        else:
            print("The operation cannot be performed.\n")

    def multiply_matrices(self):
        self.read_matrices()

        if Matrix.is_matrices_multipliable(self.dimensions_a, self.dimensions_b):
            new_matrix = self.calculate_product()
            print("The result is:")
            Matrix.print_matrix(new_matrix)
            print()
        else:
            print("The operation cannot be performed.\n")

    def calculate_product(self):
        m = self.dimensions_a[0]
        n = self.dimensions_b[1]
        p = self.dimensions_a[1]

        new_matrix = []

        for _ in range(m):
            new_row = []
            for _ in range(n):
                new_row.append(0)
            new_matrix.append(new_row)

        row_index = 0
        while row_index < m:
            col_index = 0
            while col_index < n:

                sum_ = 0
                index = 0
                while index < p:
                    sum_ += self.matrix_b[index][col_index] * self.matrix_a[row_index][index]
                    index += 1
                new_matrix[row_index][col_index] = sum_

                col_index += 1
            row_index += 1
        return new_matrix

    @staticmethod
    def transpose_choice():
        print("\n1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

        user_input = int(input("Your choice: "))
        Matrix.transpose_matrix(user_input)

    @staticmethod
    def transpose_matrix(a_transpose_dir):
        print("Enter matrix size: ", end="")
        dimensions = Matrix.get_dimensions()
        print("Enter matrix: ")
        matrix = []
        Matrix.read_matrix(matrix, dimensions)

        if a_transpose_dir == Transposition.MAIN_DIAGONAL:
            matrix = list(zip(*matrix))
        elif a_transpose_dir == Transposition.SIDE_DIAGONAL:
            matrix.reverse()
            for row in matrix:
                row.reverse()
            matrix = list(zip(*matrix))
        elif a_transpose_dir == Transposition.VERTICAL_LINE:
            for row in matrix:
                row.reverse()
        elif a_transpose_dir == Transposition.HORIZONTAL_LINE:
            matrix.reverse()

        print("The result is:")
        Matrix.print_matrix(matrix)
        print()


def run():
    app = Matrix()

    while True:
        Matrix.print_menu()
        try:
            user_input = int(input("Your choice: "))
        except ValueError:
            print("Invalid input!")
        else:
            if user_input == Menu.EXIT:
                break
            elif user_input == Menu.ADD_MATRICES:
                app.reset()
                app.add_matrices()
            elif user_input == Menu.MULTIPLY_MATRIX_CONSTANT:
                app.multiply_matrix_constant()
            elif user_input == Menu.MULTIPLY_MATRICES:
                app.reset()
                app.multiply_matrices()
            elif user_input == Menu.TRANSPOSE_MATRIX:
                app.transpose_choice()
            else:
                print("Invalid input!")


if __name__ == "__main__":
    run()
