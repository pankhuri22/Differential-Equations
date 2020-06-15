import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("petrol_prices_delhi.txt", delimiter= "\n")
x = []
for i in range(np.size(y)):
	x.append(i)
x = np.array(x)


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


def degree_one():
	A1 = x[:,np.newaxis]**[1,0]
	t1, t0 = np.linalg.lstsq(A1, y, rcond = -1)[0]	
	#print t0, t1
	t = [t1,t0]

	prod = np.dot(A1,t)
	diff = prod - y
	error = np.linalg.norm(diff)
	rel_error = error / np.linalg.norm(y)
	#print(rel_error)  #0.01592970563496064
	
	#plt.plot(x, y, 'o', label='Original data', markersize=10)
	#plt.plot(x, t[1] + t[0] *x, 'r', label='Fitted line')
	#plt.legend()
	#plt.show()
	print A1
	X = A1
	bdash = t
	Q,R = qr_decomp(X)
	
	b = np.linalg.inv(R).dot(Q.T).dot(y)
	yhat = X.dot(b)
	plt.plot(X,y,'o')
	plt.plot(X,yhat,color='red')
	plt.legend()
	#plt.show()





def degree_two():
	A2 = x[:, np.newaxis]**[2,1,0]
	t2 , t1, t0 = np.linalg.lstsq(A2,y,rcond = -1)[0]
	t = [t2,t1,t0]

	prod = np.dot(A2,t)
	diff = prod - y
	error = np.linalg.norm(diff)
	rel_error = error / np.linalg.norm(y)
	print(rel_error)  #0.015244734332359159
	'''
	plt.plot(x,y,'o', label = 'Original data', markersize = 10)
	plt.plot(x, t[2] + t[1]*x + t[0]*x**2, 'r', label = 'Fitted line')
	plt.legend()
	plt.show()
	'''

	X = A2
	bdash = t
	Q,R = qr_decomp(X)
	
	b = np.linalg.inv(R).dot(Q.T).dot(y)
	yhat = X.dot(b)
	plt.plot(X,y,'o')
	plt.plot(X,yhat,color='red')
	plt.legend()
	plt.show()

	

def degree_three():
	A3 = x[:, np.newaxis]**[3,2,1,0]
	t3,t2,t1,t0 = np.linalg.lstsq(A3,y,rcond = -1)[0]
	t = [t3,t2,t1,t0]

	prod = np.dot(A3,t)
	diff = prod - y
	error = np.linalg.norm(diff)
	rel_error = error / np.linalg.norm(y)
	print(rel_error)  #0.013952531748703603

	#plt.plot(x,y,'o', label = 'Original data', markersize = 10)
	#plt.plot(x, t[3] + t[2]*x + t[1]*x**2 + t[0]*x**3, 'r', label = 'Fitted line')
	##plt.legend()
	#plt.show()

	X = A3
	bdash = t
	Q,R = qr_decomp(X)
	
	b = np.linalg.inv(R).dot(Q.T).dot(y)
	yhat = X.dot(b)
	plt.plot(X,y,'o')
	plt.plot(X,yhat,color='red')
	plt.legend()
	plt.show()



def degree_four():
	A4 = x[:, np.newaxis]**[4,3,2,1,0]
	t4,t3,t2,t1,t0 = np.linalg.lstsq(A4,y,rcond = -1)[0]
	t = [t4,t3,t2,t1,t0]

	prod = np.dot(A4,t)
	diff = prod - y
	error = np.linalg.norm(diff)
	rel_error = error / np.linalg.norm(y)
	print(rel_error)  #0.011891820265493184

	#plt.plot(x,y,'o', label = 'Original data', markersize = 10)
	#plt.plot(x, t[4] + t[3]*x + t[2]*x**2 + t[1]*x**3 + t[0]*x**4, 'r', label = 'Fitted line')
	#plt.legend()
	#plt.show()

	X = A4
	bdash = t
	Q,R = qr_decomp(X)
	
	b = np.linalg.inv(R).dot(Q.T).dot(y)
	yhat = X.dot(b)
	plt.plot(X,y,'o')
	plt.plot(X,yhat,color='red')
	plt.legend()
	plt.show()



def degree_five():

	A5 = x[:, np.newaxis]**[5,4,3,2,1,0]
	t5,t4,t3,t2,t1,t0 = np.linalg.lstsq(A5,y,rcond = -1)[0]
	t = [t5,t4,t3,t2,t1,t0]

	prod = np.dot(A5,t)
	diff = prod - y
	error = np.linalg.norm(diff)
	rel_error = error / np.linalg.norm(y)
	print(rel_error)  #0.009899102962613272
	'''
	plt.plot(x,y,'o', label = 'Original data', markersize = 10)
	plt.plot(x, t[5] + t[4]*x + t[3]*x**2 + t[2]*x**3 + t[1]*x**4 + t[0]*x**5, 'r', label = 'Fitted line')
	plt.legend()

	plt.show()
	'''
	X = A5
	bdash = t
	Q,R = qr_decomp(X)
	
	b = np.linalg.inv(R).dot(Q.T).dot(y)
	yhat = X.dot(b)
	plt.plot(X,y,'o')
	plt.plot(X,yhat,color='red')
	plt.legend()
	plt.show()





if __name__ == '__main__' :
	n = int(input())
	if n==1 :
		degree_one()
	elif n==2 :
		degree_two()
	elif n==3 :
		degree_three()
	elif n==4 :
		degree_four()
	else :
		degree_five()				

