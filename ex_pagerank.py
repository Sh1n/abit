"""
	PageRank
	- Power Method

	- At each step i the probability of the surfer to reach a node v 
	starting from a node u is:
		pi[v] = sum[(u,v) <- E ]( (pi-1[u]) / outDegree(u) )

		considering all the incoming edges for the node v, it sums the probability
		of being of the node u and picking v among its out-degree

"""
import numpy
"""
	Testing Matrix
	Adjacency
	-----------------
		A	B	C	D
	-+---------------
	A|	0	1	0	0
	B|	1	0	1	0
	C|	0	0	0	1
	D|	1	0	0	0
"""

adjacency = [
	[0, 1, 0, 0],
	[1, 0, 1, 0],
	[0, 0, 0, 1],
	[1, 0, 0, 0]
]

"""
	Damping Factor
		Probability d of the surfer to jump on a random page 
		1 -d is the probability of the surfer to jump on a connected page
		
		1.0 -> completely random
		0.0	-> uniform distribution
"""		
d = 1.0

# Convert Scores to float
E = map (lambda x: map (float, x), adjacency)
L = numpy.array(E)

# Normalization
for row in L:
	row /= sum(row)

# The transformation matrix is actually the transpose of L
Lt = L.transpose()

# At each step the probability is computed by applying the function.
# The pagerank is given by a value array of the same leght of the nodes where
# each value represent its rank hence its "reputation"

# Base Case P0 - starting from node 0
p = numpy.zeros(len(adjacency))
p[0] = 1.0

# Apply the power iterations method by repeatedly multiplying the probability 
# distribution vector p by matrix Lt
iterationNumber = 100
print " =========== Power iterations =========="
print p
for i in xrange(iterationNumber):
	p = numpy.dot (Lt, p)
	print "[Step ", i, "] ==================="
	print p



