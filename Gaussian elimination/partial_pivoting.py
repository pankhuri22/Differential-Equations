import numpy as np

def partial_pivot(a , b,n):
	for k in range (0,n-1):
		mat = np.zeros((n,n))
		np.fill_diagonal(mat,1)
		maximum = a[k,k]
		p=k
		for i in range (k,n):
			if a[i,k]>maximum:
				maximum = a[i,k]
				p = i
		if p != k:
			temp = np.array(a[k,:])
			temp2 = np.array(a[p,:])
			a[k]=temp2
			a[p]=temp

			tt = np.array(b[k])
			tt2 = np.array(b[p])
			b[k] = tt2
			b[p] = tt

		if a[k,k]==0:
			raise RuntimeError("singular matrix")
		for i in range (k+1,n):
			mat[i,k]= -1 * a[i,k]*1.0/a[k,k]
		a = np.dot(mat,a)
		b = np.dot(mat,b)
		#print(a)
			
		

	return a,b


def back_subsitute(U, bb):
    n = U.shape[1]
    x = np.zeros(n)
    for j in range(n - 1, -1, -1):   # loop backwards over columns
        if U[j, j] == 0:
            raise RuntimeError("singular matrix")

        x[j] = bb[j] / U[j, j]
        for i in range(0, j):
            bb[i] -= U[i, j] * x[j]

    return x



if __name__ == '__main__':
    #A = np.random.randn(100,100)
    
    
	A = np.zeros(shape = (100,100))
	"""
	for i in range(0,100): 
		for j in range(0,100): 
			if(((i+2) % 100) == j): 
				A[i][j] = 5
			else : 
				A[i][j] = 0.001
	"""

	for i in range(0,100): 
		for j in range(0,100): 
			A[i][j] = 1 / (1 + abs((i+1) % (100-j))) ** 4				


	np.random.seed(2018)
	x_1, x_2, x_3 = np.random.rand(100, 3).T
	b = np.dot(A,x_3)
	sol,bb = partial_pivot(A,b,100)
	ans = back_subsitute(sol,bb)
	error = sol - x_3
	normerror = np.linalg.norm(error)
	#print(normerror)
	residual = b - np.dot(A,ans)
	rnorm = np.linalg.norm(residual)
	#print(rnorm)
	nn = np.linalg.solve(A,b)
	kk = nn - x_3
	norm = np.linalg.norm(kk)
	#print(norm)

	residuall = b-np.dot(A,nn)
	#print(np.linalg.norm(residuall))
	

#error = 379.3831452058622
#norm = 1.6621266034192004e-13  
# 6th poart A1 =  1.310617922383716e-13

#A2 ans
#error#residual#6th part
#73.8879549215215
#2.032554939699295e-14
#2.705869477390394e-15

#A3 ans

#60.32675801089301
#1.7342238036525468e-15
#4.155557514143405e-15