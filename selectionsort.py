A = [7,2,9,4,7,3,8,9,4,6,3,6,8]

def selectionsort(X):
	for i in xrange(len(X)):
		min_ind = i
		for j in xrange(i+1, len(X)):
			if X[j] < X[min_ind]:
				min_ind = j
		X[i], X[min_ind] = X[min_ind], X[i]		
	return X

print selectionsort(A)		