A = [2,7,5,4,7,1,0,8,9,3,2]

def heapsort(X):
	length = len(X) - 1
	leastparent = length/2
	for i in xrange(leastparent,-1,-1):
		movedown(X,i,length)
	for i in xrange(length,0,-1):
		if X[0] > X[i]:
			A[0],A[i] = A[i], A[0]
			movedown(X,0,i-1)
	return X

def movedown(Y,first,last):
	largest = 2*first + 1
	while (largest <= last):
		if (largest < last) and (Y[largest] < Y[largest + 1]):
			largest += 1
		if (Y[largest] > Y[first]):
			Y[largest], Y[first] = Y[first], Y[largest]
			first = largest
			largest = 2*first + 1
		else:
			return Y
	return Y

print heapsort(A)	

