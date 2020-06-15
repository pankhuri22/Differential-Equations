import numpy as np
import scipy.sparse as sp
import time
def power_iteration(AA):
 tol = 10**(-12)
 A = AA - 2*np.eye(AA.shape[0])
 x = np.random.rand(np.shape(A)[0])
 
 count = 0
 v = [x]
 ratio = 10
 #x = np.random.rand(A.shape[0])
 eigval_old = np.dot(np.transpose(x),A.dot(x))/np.dot(np.transpose(x),x)  
 k = 1
 while ratio > tol :
    y = np.linalg.solve(A,v[k-1])  
    x = y / np.linalg.norm(y,np.inf) 
    ratio = np.linalg.norm(x-v[k-1])/np.linalg.norm(v[k-1])
    count = count + 1
    v.append(x)
    k = k+1
 eigval_new = np.dot(np.transpose(x),A.dot(x))/np.dot(np.transpose(x),x)
 '''
 if(abs(eigval_new-eigval_old)/eigval_new) < tol :
    return eigval_new
 eigval_old = eigval_new
 '''
 return count ,x, eigval_new


if __name__ == '__main__' :
	#for i in range(10):
	  #np.random.seed(i)
	  AA = np.array([[6,2,1],[2,3,1],[1,1,1]])
	  count, eigv, eig  =power_iteration(AA)
	  seig = 2 + eig
	  print count, eigv,seig


#how to implement with shift. what is shift ? and also how to find nearest to 2   


'''
13 [-0.60692002  1.          0.34691451] 2.133074475348525
13 [-0.60692002  1.          0.34691451] 2.133074475348525
14 [ 0.60692002 -1.         -0.34691451] 2.133074475348525
9 [-0.60692002  1.          0.34691451] 2.133074475348525
14 [-0.60692002  1.          0.34691451] 2.133074475348525
13 [-0.60692002  1.          0.34691451] 2.133074475348525
14 [-0.60692002  1.          0.34691451] 2.133074475348525
13 [-0.60692002  1.          0.34691451] 2.133074475348525
13 [-0.60692002  1.          0.34691451] 2.133074475348525
13 [-0.60692002  1.          0.34691451] 2.133074475348525
'''

'''
12 [-0.60692002  1.          0.34691451] 2.133074475348525
'''
