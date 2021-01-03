def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def is_equal_dimensions(matrix_a, matrix_b):
    size_a = ""
    size_b = ""
    for row in matrix_a:
        size_a += str(len(row))
    for row in matrix_b:
        size_b += str(len(row))

    if size_a != size_b:
        return False
    return True


def sum_matrices(matrix_a, matrix_b):
    if not is_equal_dimensions(matrix_a, matrix_b):
        return []

    for row in range(len(matrix_a)):
        for col in range(len(matrix_a[0])):
            matrix_a[row][col] += matrix_b[row][col]
    return matrix_a


def read_matrix(matrix, size):
    rows = size[0]
    # cols = size[1]
    for _ in range(rows):
        new_row = [int(x) for x in input().split(' ')]
        matrix.append(new_row)


matrix_size_1 = [int(x) for x in input().split(' ')]
matrix_1 = []
read_matrix(matrix_1, matrix_size_1)
matrix_size_2 = [int(x) for x in input().split(' ')]
matrix_2 = []
read_matrix(matrix_2, matrix_size_2)

if is_equal_dimensions(matrix_1, matrix_2):
    new_matrix = sum_matrices(matrix_1, matrix_2)
    print_matrix(new_matrix)
else:
    print("ERROR")
