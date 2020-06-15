import numpy as np
from prettytable import PrettyTable


def gauss(A, b, n):
    for row in range(0, n-1):
        factor = np.identity(n)

        if A[row][row]==0:
            break
        for i in range(row+1, n):
            factor[i][row] = -1 * A[i,row] / A[row,row]
            #b[i]() = b[i] - factor * b[row]
          #  print(factor)
           # print(A)
        A = np.dot(factor,A) 
        b = np.dot(factor,b) 
    return A,b      


def back_subsitute(U, bb):
    n = U.shape[1]
    x = np.zeros(n)
    for j in range(n - 1, -1, -1):   # loop backwards over columns
        if U[j, j] == 0:
            continue

        x[j] = bb[j] / U[j, j]
        for i in range(0, j):
            bb[i] -= U[i, j] * x[j]

    return x


# Main program starts here
if __name__ == '__main__':
    #A = np.random.randn(100,100)
    A = np.zeros(shape = (100,100))

    for i in range(0,100): 
        for j in range(0,100): 
            A[i][j] = 1 / (1 + abs((i+1) % (100-j))) ** 4   

    

    #print(np.linalg.cond(A))
 
    np.random.seed(2018)
    x_1, x_2, x_3 = np.random.rand(100, 3).T
    b = np.dot(A,x_3)

    p,B = gauss(A, b,100)
    y = back_subsitute(p,B)

    #   print('Gauss result is x = \n %s' % x)
    error = y - x_3
    normerror = np.linalg.norm(error)
    #print(normerror)
    residual = b - np.dot(A,y)
    rnorm = np.linalg.norm(residual)
    #print(rnorm)


t = PrettyTable(['Condition number', 'Error un-pivoted ' , 'Residual un-pivoted solve' , 'Error partially-pivoted', 'Residual partially-pivoted solve', 'Error np.linalg.solve','Residual np.linalg.solve'])
t.add_row(['101.15054281812272', '2.1493530534593304e-12', '5.812876806939427e-12 ' , '379.3831452058622' , '1.6621266034192004e-13 ','1.310617922383716e-13','2.082963028648268e-15'])
t.add_row(['1.0200040008001612', 'failed', 'failed ' , '73.8879549215215','2.032554939699295e-14','2.705869477390394e-15','2.2644195468014703e-15'])
t.add_row(['123.60138082680795', '7.77409933283912', '82.58499433845904' , '60.32675801089301 ','1.7342238036525468e-15','4.155557514143405e-15','2.4424906541753444e-15'])

print(t)

# A1 ans 
#2.1493530534593304e-12 = 
#5.812876806939427e-12 = residue
#101.15054281812272 = cond

#A2 ans
# 1.0200040008001612