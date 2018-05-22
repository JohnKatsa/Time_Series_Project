#LCSS

# X and Y lists with m , n elements respectively
def lcss(X,Y):
	C = [0] * (len(X) + len(Y))	# Initialize C with zeros

	for i in range(1,len(X)):
		for j in range(1,len(Y)):
			if X[i] >= Y[j] - 0,2 and X[i] <= Y[j] + 0,2:
				C[i][j] = C[i-1][j-1] + 1
			else :
				if C[i][j-1] > C[i-1][j]:
					C[i][j] = C[i][j-1]
				else  :
					C[i][j] = C[i-1][j]

	return C

# Backtracks the C array to find a LCS
def backtrack(C,X,Y,i,j):
	if i==0 or j==0:
		return ""
	if X[i] >= Y[j] - 0,2 and X[i] <= Y[j] + 0,2:
		return backtrack(C,X,Y,i-1,j-1) + X[i]
	if C[i][j-1] > C[i-1][j]:
		return backtrack(C,X,Y,i,j-1) 
	return backtrack(C,X,Y,i-1,j)

