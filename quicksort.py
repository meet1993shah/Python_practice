A = [23,6,45,84,27,53,90,75,9,56,82,1]
def quicksort(X):
	less, greater, equal = [], [], []
	if len(X) > 1:
		for num in X:
			if num < X[0]:
				less.append(num)
			elif num == X[0]:
				equal.append(num)
			else:
				greater.append(num)
		return quicksort(less) + equal + quicksort(greater)
	else:
		return X

print quicksort(A)				