A = [7,2,9,4,7,3,8,9,4,6,3,6,8]

def insertionsort(X):
	for i in xrange(1, len(X)):
		ind= X[i]
		j = i
		while(j > 0 and X[j-1] > ind):
			X[j] = X[j-1]
			j-=1
		X[j] = ind
	return X

print insertionsort(A)
