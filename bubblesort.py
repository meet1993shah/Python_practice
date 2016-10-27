A = [7,2,9,4,7,3,8,9,4,6,3,6,8]

def bubblesort(X):
	for i in xrange(len(X)):
		for j in xrange(1,len(X) - i):
			if X[j] <= X[j-1]:
				X[j], X[j-1] = X[j-1], X[j]
	return X

print bubblesort(A)	


