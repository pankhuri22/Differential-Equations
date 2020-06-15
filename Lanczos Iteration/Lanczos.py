import numpy as np
import random
import matplotlib.pyplot as plt

def lanc(A) :
	b = np.zeros(n)
	q = np.zeros((n,n))
	


def Lanczos( A, v, m=100 ):
    n = len(v)
    zzo=[]
    zzoy = []
    V = np.zeros((m,n))
    T = np.zeros((m,m))
    vo   = np.zeros(n)
    beta = 0
    for j in range( 0,m-1 ):
        w    = np.dot( A, v )
        alfa = np.dot( np.transpose(v),w )
        w    = w - (alfa * v) - (beta * vo)
        beta = np.linalg.norm(w) 
        if beta < 10**(-15) :
        	break
        vo   = v
        v    = w / beta 
        V[j,:]   = v
        T[j,j  ] = alfa 
        T[j+1,j] = beta
        T[j,j+1] = beta

        zzo.append(np.linalg.eigvals(T))
        zzoy.append(j)

        if beta < 10**(-15) :
        	break
    return T, V,zzo,zzoy


def ans_part1():
	n=100
	b = np.random.randn(n,n)
	A = b+ b.T

	np.random.seed(0)
	v0 = np.random.rand(n)
	v0 /= np.linalg.norm(v0) 
	H,Q = Lanczos(A,v0 , 100)

	

	QQt = np.dot(Q,Q.T)
	I = np.eye((100))
	diff = QQt- I
	n = np.dot(Q.T,np.dot(A,Q))
	diff2 = n-H
	norm = np.linalg.norm(diff2)

	first = np.linalg.norm(diff)
	second = norm / np.linalg.norm(A)

	#return Q

	print first
	print second


def ans_part2():
	n=100
	B = np.random.rand(n,n)
	Q,R = np.linalg.qr(B)
	D = []
	for i in range(1,n+1):
		D.append(i)	

	DD = np.diag(D)	
	A = np.dot(Q,np.dot(DD,np.transpose(Q)))
	q = np.random.randn(100)
	q = q / np.linalg.norm(q)
	T,V,zzo,zzoy = Lanczos(A,q,m=100)
	#print np.linalg.eigvals(T)
	#print zzoy
	return zzo, zzoy



q = ans_part1()
print q

X,Y=ans_part2()
plt.plot(X,Y,'o',markersize=2)
plt.xlim(0,120)
plt.show()
