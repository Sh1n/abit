import math
import re
# Jaccard Implementation

# training -> vengono inseriti tutti gli esempi
voucabolary = []	# term -> indice colonna
dindex		= []	# document -> indice riga
data		= []	# matrice termini/documenti tf-idf weighted

def tokenize(document):
	return re.findall(r"[\w]+", document)

def stems(terms):
	return terms

def stopword_remove(terms):
	return terms

def update_voucabolary(terms):
	for term in terms:
		if term not in voucabolary:
			voucabolary.append(term)

def update_dindex(document, terms):
	dindex.append({ "phrase": document, "terms": terms })

def zero_matrix(rows, cols):
	return [[0] * cols for row in xrange(rows)]

def print_matrix(matrix):
	for row in matrix:
		print row

def index_by_presence():
	global data
	data = zero_matrix(len(voucabolary), len(dindex))	
#	for document in dindex:
	for i in xrange(len(dindex)):
		for j in xrange(len(voucabolary)):
			if voucabolary[j] in dindex[i]["terms"]:
				data[j][i] = 1

def index_by_occurrences():
	global data
	data = zero_matrix(len(voucabolary), len(dindex))	
#	for document in dindex:
	for i in xrange(len(dindex)):
		for j in xrange(len(voucabolary)):
			if voucabolary[j] in dindex[i]["terms"]:
				data[j][i] = dindex[i]["terms"].count(voucabolary[j])

"""
	TF-IDF
"""

def get_documents_by_term(term):
	global dindex
	return [document for document in dindex if term in document["terms"]]	

def tf(term, documentTerms):
	return documentTerms.count(term)

def idf(term):
	global dindex
	return math.log ( float(len(dindex)) / float(len(get_documents_by_term(term))) )

def index_by_tfidf():
	global data
	data = zero_matrix(len(voucabolary), len(dindex))
	for i in xrange(len(dindex)):
		for j in xrange(len(voucabolary)):
			if voucabolary[j] in dindex[i]["terms"]:
				data[j][i] = tf(voucabolary[j], dindex[i]["terms"]) * idf(voucabolary[j])


def print_matrix_corpora():
	global data
	line = "\t\t"
	for i in xrange(len(dindex)):
		line += `i` + "\t"
	print line
	for j in xrange(len(voucabolary)):
		line = voucabolary[j] + "\t\t"
		for i in xrange(len(dindex)):
			line += `data[j][i]` + "\t"
		print line

def learn(corpora):
	#for each string
		# tokenize, stems, removes stopwords
		# update voucabolary
	for document in corpora:
		terms = stopword_remove(stems(tokenize(document)))	
		update_voucabolary(terms)
		update_dindex(document,terms)
	index_by_tfidf()

"""
	Retrieval
"""
def jaccard_score(A,B):
	x = float(len( set(A).intersection(set(B))))
	y = float(len(set(A).union(set(B))))
	return x/y

def find(query):
	# computes the jaccard score for each sentence
	queryTerms = stopword_remove(stems(tokenize(query)))
	bestScore = 0.0
	bestDocument = ""
	
	for document in dindex:
		score = jaccard_score(queryTerms, document["terms"])
		if score > bestScore:
			bestScore = score
			bestDocument = document["phrase"]
		
	print "Best Result: ", bestDocument, "(" , bestScore, ")"

corpora = []
corpora.append("alice loves bob, but bob doesn't love alice")
corpora.append("alice loves loves loves tomato")
corpora.append("man in the middle")
corpora.append("sparse matrix")
corpora.append("hello, this is an example phrase for the tokenizer")
corpora.append("alice loves bob and tomato")

learn(corpora)


print_matrix_corpora()

#find(query)

query = "alice and bob"

find_by_dot_product(query)
