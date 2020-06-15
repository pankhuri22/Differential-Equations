import numpy as np

def qr_iteration(a,tol):
	iterations = 500
	m = a.shape[0]; 
	eigv = np.zeros(m)
	n = m-1
	while n>0:
		count = 0
		while max(a[n,0:n]) > tol and count < iterations:
		#while count < iterations:
			u = a[n,n]
			yo = 0;	
			x1= np.eye(n+1)
			x2=np.eye(n+1)
			q,r = np.linalg.qr(a - u*x1)
			a = u*x2+ np.dot(r,q) 
			count = count +1 
			yo = yo + 1
		for i in range(n):
			print i	
		if count < iterations:	
			eigv[n]=a[n,n]		
			a = a[:n+1,:n+1]
			n -= 1					
	if n==0: 
		eigv[0] = a[0,0]
		print eigv 
	else : 
		pass	
		
	return eigv


A = np.array([[2,3,2],[10,3,4],[3,6,1]])

'''
Computed eigenvalues:  [11. -3. -2.]
Actual eigenvalues:  [11. -2. -3.]
'''

B = np.array([[6,2,1],[2,3,1],[1,1,1]])

'''
Computed eigenvalues:  [7.28799214 2.13307448 0.57893339]
Actual eigenvalues:  [7.28799214 2.13307448 0.57893339]
'''
tol = 10**(-16)
eigenvalues_1 = qr_iteration(A.copy(),tol)
print "Computed eigenvalues: ", eigenvalues_1
print "Actual eigenvalues: ", np.linalg.eigvals(A)

'''
eigenvalues_1 = qr_iteration(B.copy(),tol)
print "Computed eigenvalues: ", eigenvalues_1
print "Actual eigenvalues: ", np.linalg.eigvals(B)
'''


