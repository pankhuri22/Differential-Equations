import numpy as np

def qr_decomp(A):
	n = np.size(A,1)
	m = np.size(A,0)

	q = np.zeros((m,n))
	r = np.zeros((n,n))

	for j in range(0,n):
		v = A[:,j]
		if j>0 :
			for i in range(0,j):
				r[i,j] = np.inner(np.transpose(q[:,i]),A[:,j])
				v = v - np.dot(r[i,j],q[:,i])
		r[j,j] = np.linalg.norm(v)
		q[:,j] = v/r[j,j]	

	return q,r


def rel_error(Q,R,A):
	product = np.dot(Q,R)
	diff = product - A
	error = np.linalg.norm(diff)
	na = np.linalg.norm(A)
	rel_error = error/na
	return rel_error

def con_no(Q,R,A):
	product = np.dot(Q,R)
	return np.linalg.cond(product)	, np.linalg.cond(A)

#A = np.array([[2,-2,18],[2,1,0],[1,2,0]])

A = np.random.rand(100,80)
#B = np.random.rand(10,10)
#C = np.random.rand(100,80)
Aq, Ar = qr_decomp(A)	
print np.shape(A), np.shape(Aq), np.shape(Ar)
#Bq, Br = qr_decomp(B)	
#Cq, Cr = qr_decomp(C)
print " "
Aerror = rel_error(Aq,Ar,A)
print Aerror
#Berror = rel_error(Bq,Br,B)
#Cerror = rel_error(Cq,Cr,C)
print "yoooo"
#Aqrcond , Acond = con_no(Aq,Ar,A)
#Bqrcond , Bcond = con_no(Bq,Br,B)
#cqrcond , ccond = con_no(Cq,Cr,C)
print np.linalg.cond(A)
print " Qcond0"
print np.linalg.cond(Aq)
print np.linalg.cond(Ar)
#print(Aq)
'''
[[ 0.04076158  0.7107056   0.33798966  0.50804891  0.3476857 ]
 [ 0.5445597   0.20116988  0.4934582  -0.24234706 -0.60062661]
 [ 0.45790463 -0.32760533 -0.26925337  0.75018169 -0.21846773]
 [ 0.65889605 -0.1867449   0.03393216 -0.27532976  0.67381338]
 [ 0.24077495  0.55877484 -0.75406447 -0.2111283  -0.12887868]]

 '''
