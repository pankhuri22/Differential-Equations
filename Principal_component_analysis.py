import numpy as np 
import matplotlib.pyplot as plt

def make_data(dims=2, npts=3000):
	np.random.seed(13)
	mix_mat = np.random.randn(dims, dims)
	mean = np.random.randn(dims)
	return np.dot(mix_mat,np.random.randn(dims, npts)) + mean[:, np.newaxis]


data = (make_data(2,3000))
X = data[0,:]
Y = data[1,:]

#plt.plot(X,Y,'o',markersize=2,color='red')	
#plt.show()

x = np.mean(X)
copy_x = X.copy()
for i in range(X.shape[0]):
	copy_x[i] = copy_x[i] - x

y = np.mean(Y)
copy_y = Y.copy()
for i in range(Y.shape[0]):
	copy_y[i] = copy_y[i] - y

dd = [copy_x, copy_y]
dd = np.array(dd)
dd = dd /  np.sqrt(5999)

u,s,v = np.linalg.svd(dd,full_matrices=False)
sigma = np.diag(s)
us = u*s
print x,y
print us[0,0] , us[1,0]

def partb():
	plt.gca().set_aspect("equal")
	plt.plot(X,Y,'o',markersize=2.0,color='lemonchiffon')
	left, right = plt.xlim()
	l,r = plt.ylim()
	plt.ylim((-1,3))  # return the current xlim
	plt.xlim((-1, 4)) 
	plt.arrow(x,y,us[0,0],us[1,0],width=0.05, fc='black', ec='black')
	plt.arrow(x,y,us[0,1],us[1,1],width=0.05, fc='black', ec='black')
	plt.show()

def partc() :
	dot = np.dot(np.dot(u,sigma),v)
	print (np.linalg.norm(dot-dd))/np.linalg.norm(dd)
#4.391900609230045e-16


def partd() :	
	sdash = s.copy()
	sdash[1,] = 0
	uss = u*sdash
	sigma_ = np.diag(sdash)
	ydash = np.dot(np.dot(u,sigma_),v)
	new_y = ydash * np.sqrt(2999)

	X_new = new_y[0,:] + np.mean(new_y[0,:])
	Y_new = new_y[1,:] + np.mean(new_y[1,:])
	plt.gca().set_aspect("equal")
	plt.plot(X,Y,'o',markersize=2.0,color='lemonchiffon')
	left, right = plt.xlim()
	l,r = plt.ylim()
	plt.ylim((-1,3))  # return the current xlim
	plt.xlim((-1, 4)) 
	plt.arrow(np.mean(new_y[0,:]),np.mean(new_y[1,:]),uss[0,0],uss[1,0],width=0.03,head_width=0.003, head_length=0.005, fc='black', ec='black')
	plt.arrow(np.mean(new_y[0,:]),np.mean(new_y[1,:]),uss[0,1],uss[1,1],width=0.03,head_width=0.003, head_length=0.005, fc='black', ec='black')
	plt.show()


