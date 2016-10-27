A = [2,5,6,8,4,6,7,2,8,5]

def mergesort(X):
	if len(X) > 1:
		mid = len(X)//2
		lefthalf = X[:mid]
		righthalf = X[mid:]
		mergesort(lefthalf)
		mergesort(righthalf)
		i=j=k=0
		while (i < len(lefthalf) and j < len(righthalf)):
			if lefthalf[i] < righthalf[j]:
				X[k] = lefthalf[i]
				i+=1
			else:
				X[k] = righthalf[j]
				j+=1
			k+=1
		while (i < len(lefthalf)):
			X[k] = lefthalf[i]
			i+=1
			k+=1
		while (j < len(righthalf)):
			X[k] = righthalf[j]
			j+=1
			k+=1			
	return X

print mergesort(A)	
