#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))


if __name__ == "__main__":
    # Test code
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()  # Test with default empty matrix
