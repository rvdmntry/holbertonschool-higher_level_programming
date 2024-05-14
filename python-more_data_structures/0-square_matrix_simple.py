#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	# Create a new matrix of the same size with squared values
	new_matrix = [[element ** 2 for element in row] for row in matrix]
	return new_matrix
