"""
	Generic Helper class for matrix management
"""
import numpy

# Creates an NxN zero matrix
def zero_matrix (n):
	return [[0] * n for i in xrange(n)]

# Creates a NxN defined matrix
def defined_matrix(n, v):
	return [[v] * n for i in xrange(n)]

# creates a diagonal NxN matrix 
def eye_matrix(n):
	return [ [0 if (i != j) else 1 for j in xrange(n)] for i in xrange(n)]

# given a graph (adjacency matrix) creates a bipartite components
def set_bipartite_component (matrix, from, to):
	for i in from:
		for j in to:
			matrix[i][j] = 1

# Computes the out-degree of a single node (sum on the outgoing edges)
def out_degree(matrix, node):
	return sum(matrix[node])
