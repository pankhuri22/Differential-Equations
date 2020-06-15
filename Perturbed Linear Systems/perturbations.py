import numpy as np
import matplotlib.pyplot as plt

A = 2 * np.identity(512)
c = -1 * np.ones(511)
np.fill_diagonal(A[:,1:],c)
np.fill_diagonal(A[1:],c)

A.shape = (512,512)
cond = np.linalg.cond(A) 
output = cond


print("condition no of A : " + str(cond))


b = []
bv = np.random.randn(512)
bnorm = np.linalg.norm(bv)

b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)
b.append(bv/bnorm)

for i in range(10):
	b[i].shape = (512,1)

print("random vectors b stored in an array b : " + str(b))	

##---------------------------------------------------------------------------------------------

# for b1 all the x and x' and corresponding perturbations and finally appended to x axis

perturbations1 = []
for i in range(10):
    perturbations1.append((i+1)*0.01*b[0])

x1 = np.linalg.solve(A,b[0])

xx1 = []
for k in range(10):
	xx1.append(np.linalg.solve(A,perturbations1[k]))


Xaxis = []
for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx1[j])) / (np.linalg.norm(x1))))

Yaxis = []
for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations1[j]) / np.linalg.norm(b[0])))

print("perturbations1 : " + str(perturbations1))

##---------------------------------------------------------------------------------------------

perturbations2 = []
for i in range(10):
    perturbations2.append((i+1)*0.01*b[1])

x2 = np.linalg.solve(A,b[1])

xx2 = []
for k in range(10):
	xx2.append(np.linalg.solve(A,perturbations2[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx2[j])) / (np.linalg.norm(x2))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations2[j]) / np.linalg.norm(b[1])))

print("perturbations2 : " + str(perturbations2))


##---------------------------------------------------------------------------------------------

perturbations3 = []
for i in range(10):
    perturbations3.append((i+1)*0.01*b[2])

x3 = np.linalg.solve(A,b[2])

xx3 = []
for k in range(10):
	xx3.append(np.linalg.solve(A,perturbations3[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx3[j])) / (np.linalg.norm(x3))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations3[j]) / np.linalg.norm(b[2])))

print("perturbations3 : " + str(perturbations3))


##---------------------------------------------------------------------------------------------

perturbations4 = []
for i in range(10):
    perturbations4.append((i+1)*0.01*b[3])

x4 = np.linalg.solve(A,b[3])

xx4 = []
for k in range(10):
	xx4.append(np.linalg.solve(A,perturbations4[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx4[j])) / (np.linalg.norm(x4))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations4[j]) / np.linalg.norm(b[3])))

print("perturbations4 : " + str(perturbations4))


##---------------------------------------------------------------------------------------------
#5
perturbations5 = []
for i in range(10):
    perturbations5.append((i+1)*0.01*b[4])

x5 = np.linalg.solve(A,b[4])

xx5 = []
for k in range(10):
	xx5.append(np.linalg.solve(A,perturbations5[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx5[j])) / (np.linalg.norm(x5))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations5[j]) / np.linalg.norm(b[4])))

print("perturbations5 : " + str(perturbations5))


##---------------------------------------------------------------------------------------------
#6
perturbations6 = []
for i in range(10):
    perturbations6.append((i+1)*0.01*b[5])

x6 = np.linalg.solve(A,b[5])

xx6 = []
for k in range(10):
	xx6.append(np.linalg.solve(A,perturbations6[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx6[j])) / (np.linalg.norm(x6))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations6[j]) / np.linalg.norm(b[5])))

print("perturbations6 : " + str(perturbations6))


##---------------------------------------------------------------------------------------------
#7
perturbations7 = []
for i in range(10):
    perturbations7.append((i+1)*0.01*b[6])

x7 = np.linalg.solve(A,b[6])

xx7 = []
for k in range(10):
	xx7.append(np.linalg.solve(A,perturbations7[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx7[j])) / (np.linalg.norm(x7))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations7[j]) / np.linalg.norm(b[6])))

print("perturbations7 : " + str(perturbations7))


##---------------------------------------------------------------------------------------------
#8

perturbations8 = []
for i in range(10):
    perturbations8.append((i+1)*0.01*b[7])

x8 = np.linalg.solve(A,b[7])

xx8 = []
for k in range(10):
	xx8.append(np.linalg.solve(A,perturbations8[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx8[j])) / (np.linalg.norm(x8))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations8[j]) / np.linalg.norm(b[7])))

print("perturbations8 : " + str(perturbations8))


##---------------------------------------------------------------------------------------------
#9

perturbations9 = []
for i in range(10):
    perturbations9.append((i+1)*0.01*b[8])

x9 = np.linalg.solve(A,b[8])

xx9 = []
for k in range(10):
	xx9.append(np.linalg.solve(A,perturbations9[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx9[j])) / (np.linalg.norm(x9))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations9[j]) / np.linalg.norm(b[8])))

print("perturbations9 : " + str(perturbations9))


##---------------------------------------------------------------------------------------------
#10
 
perturbations10 = []
for i in range(10):
    perturbations10.append((i+1)*0.01*b[9])

x10 = np.linalg.solve(A,b[9])

xx10 = []
for k in range(10):
	xx10.append(np.linalg.solve(A,perturbations10[k]))

for j in range(10):
	Xaxis.append(cond * ((np.linalg.norm(xx10[j])) / (np.linalg.norm(x10))))

for j in range(10):
	Yaxis.append((np.linalg.norm(perturbations10[j]) / np.linalg.norm(b[9])))
print("perturbations10 : " + str(perturbations10))


plt.figure(1, figsize=(9, 3))
plt.plot(Xaxis, Yaxis,'ko')
plt.show()