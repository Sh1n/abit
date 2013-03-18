"""
	HITS
	- In the HITS algorithm the matrix is divided into two clusters. Root
	set and expanded set. Ones are said to be the HUBs and the other
	authorities. In particoular:
		- HUB: reference other document
		- AUTHORITY: document referenced
	Since each document can link and be linked, each of them as a score made by
	both authority score and hub one. Hence we are going to have two score 
	vectors of the same lenght corresponding to the number of considered nodes.

	- Computation:	at each step the hub score is given by the sum of the 
	authority scores of referenced documents. Authority one is given by the
	sum of the hub score of referencing documents.
	
	the Vector of score H at step t is given by: H^t = E * A^t-1 
	while authorities scores are A^t = E^T * H^t-1

"""
import numpy as np

"""
	Testing Matrix
	Adjacency
	-----------------
		A	B	C	D
	-+---------------
	A|	0	1	1	1
	B|	0	0	1	1
	C|	0	0	0	1
	D|	0	0	0	0
"""
adjacency = [
	[0, 1, 1, 1],
	[0, 0, 1, 1],
	[0, 0, 0, 1],
	[0, 0, 0, 0]
]

print "Adjacency Matrix"

# We create the scores, initially all scores are set to 1
n = len(adjacency)
H = [1.0 for x in range(n)]
A = [1.0 for x in range(n)]
# Number of iterations
iterations = 4


# at each iteration we update the scores / no normalization
for i in range(iterations):
	htmp = H[:]
	atmp = A[:]
	# Computing t-h : hi = SUM(j=[1:N] e(i,j)*a(j)t-1
	for i in range (n):
		H[i] = sum([adjacency[i][j] * atmp[j] for j in range(n)])	# scores of auth outgoing i -> j
	for i in range(n):
		A[i] = sum([adjacency[j][i] * htmp[j] for j in range(n)])	# scores of hub incoming i <- j 

print "HUB Scores"
print H
print "Auth Scores"
print A
print "Scores H,A"

"""
def hits_score(matrix, iterations=4, normalize=True, show=True):
	n = len(matrix)
	H = [1.0 for x in range(n)]
	A = [1.0 for x in range(n)]
	for t in range(iterations):
		atmp = A[:]
		htmp = H[:]	
		# Computing t-h : hi = SUM(j=[1:N] e(i,j)*a(j)t-1		
		for i in range(n):
			H[i] = sum([matrix[i][j] * atmp[j] for j in range(n)])
		# Computing t-a : ai = SUM(j=[1:N] e(j,i)*h(j)t-1		
		for i in range(n):
			A[i] = sum([ matrix[j][i] * htmp[j] for j in range(n)])
		if normalize:
			for i in range(n):
				H[i] = H[i] / sum(H)
				A[i] = A[i] / sum(A)
		if show:
			print "Iteration ", t
			print "Authority values: \t", a
			print "Hubs values: \t", h 
	return H, A
"""

def hits_score(matrix, iterations=4, normalize=True, show=True):
	n = len(matrix)
	H = np.ones(n)
	A = np.ones(n)
	E = np.array(matrix)
	Et = E.transpose()
	for t in range(iterations):
		H, A = np.dot (E, A), np.dot (Et, H)
		if normalize:
			for i in range(n):
				H /= sum(H)				
				A /= sum(A)				
		if show:
			print "Iteration ", t
			print "Authority values: \t", a
			print "Hubs values: \t", h 
	return H, A

print hits_score(adjacency, 3, True, False)

