import numpy as np

def rqi(A,x):
	tol = 10**(-12)
	I = np.eye(A.shape[0])
	count  = 0
	shift =  0
	v= [x]
	ratio = 50
	k=1
	while ratio > tol :
		count = count +1 
	
		shift = np.dot(v[k-1].T, np.dot(A,v[k-1]))/np.dot(v[k-1].T,v[k-1])
		try : 
			xx = np.linalg.solve(A-shift*I,v[k-1])
			u = xx/np.linalg.norm(xx)

			ratio = np.linalg.norm(u-v[k-1])/ np.linalg.norm(v[k-1])
			v.append(u)
			k = k+1
		except : 
			print "singular"
			break 	
	
	return count,shift, x/np.linalg.norm(x,np.inf)

if __name__ == '__main__' :
	for i in range(10):
	  np.random.seed(i)
	  A = np.array([[6,2,1],[2,3,1],[1,1,1]])
	  x = np.random.rand(np.shape(A)[0])

	  count, eig, eigv  =rqi(A,x)
	  print count,eig,eigv

