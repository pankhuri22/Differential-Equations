# part (i)

import numpy as np
from prettytable import PrettyTable


n = 100
np.random.seed(1729)
A = np.random.randn(n,n)
x = np.ones(n)
b = np.dot(A,x)
D = np.identity(n)
A1 = np.dot(A,D)
b1 = np.dot(b,D)
x1 = np.linalg.solve(A1,b1)
residual = b - np.dot(A,x1)
normA =np.linalg.norm(A)
normx1 = np.linalg.norm(x1)
normresidual = np.linalg.norm(residual)
RR = normresidual / (normA * normx1)
error = x1 -x 
normx =np.linalg.norm(x)
normerror = np.linalg.norm(error)
RE = normerror / normx
cond = np.linalg.cond(A1)


# ----------------------------------------------------------------------------------
# part (ii)

import numpy as np
n = 100
np.random.seed(1729)
A = np.random.randn(n,n)
x = np.ones(n)
b = np.dot(A,x)
D = np.diag(2 * np.ones(n))
A1 = np.dot(A,D)
b1 = np.dot(b,D)
x1 = np.linalg.solve(A1,b1)
residual = b - np.dot(A,x1)
normA =np.linalg.norm(A)
normx1 = np.linalg.norm(x1)
normresidual = np.linalg.norm(residual)
RR = normresidual / (normA * normx1)
error = x1 -x 
normx =np.linalg.norm(x)
normerror = np.linalg.norm(error)
RE = normerror / normx
cond = np.linalg.cond(A1)


# ----------------------------------------------------------------------------------
# part (iii)

import numpy as np
n = 100
np.random.seed(1729)
A = np.random.randn(n,n)
x = np.ones(n)
b = np.dot(A,x)
D = np.diag(np.linspace(1, 100, 100))
A1 = np.dot(A,D)
b1 = np.dot(b,D)
x1 = np.linalg.solve(A1,b1)
residual = b - np.dot(A,x1)
normA =np.linalg.norm(A)
normx1 = np.linalg.norm(x1)
normresidual = np.linalg.norm(residual)
RR = normresidual / (normA * normx1)
error = x1 -x 
normx =np.linalg.norm(x)
normerror = np.linalg.norm(error)
RE = normerror / normx
cond = np.linalg.cond(A1)


# ----------------------------------------------------------------------------------
# part (iv)

import numpy as np
n = 100
np.random.seed(1729)
A = np.random.randn(n,n)
x = np.ones(n)
b = np.dot(A,x)
D = np.diag(np.linspace(1, 10000, 100))
A1 = np.dot(A,D)
b1 = np.dot(b,D)
x1 = np.linalg.solve(A1,b1)
residual = b - np.dot(A,x1)
normA =np.linalg.norm(A)
normx1 = np.linalg.norm(x1)
normresidual = np.linalg.norm(residual)
RR = normresidual / (normA * normx1)
error = x1 -x 
normx =np.linalg.norm(x)
normerror = np.linalg.norm(error)
RE = normerror / normx
cond = np.linalg.cond(A1)


# ----------------------------------------------------------------------------------
# part (v)

import numpy as np
n = 100
np.random.seed(1729)
A = np.random.randn(n,n)
x = np.ones(n)
b = np.dot(A,x)
D = np.diag(2**-np.arange(-n//2, n//2, dtype=np.float64))
A1 = np.dot(A,D)
b1 = np.dot(b,D)
x1 = np.linalg.solve(A1,b1)
residual = b - np.dot(A,x1)
normA =np.linalg.norm(A)
normx1 = np.linalg.norm(x1)
normresidual = np.linalg.norm(residual)
RR = normresidual / (normA * normx1)
error = x1 -x 
normx =np.linalg.norm(x)
normerror = np.linalg.norm(error)
RE = normerror / normx
cond = np.linalg.cond(A1)
 

t = PrettyTable(['S.No', 'Relative Residual' , 'Relative Error' , 'Condition No'])
t.add_row(['1', '1.382432056116166e-16', '1.6033480990702738e-14 ' , '324.3452969109414'])
t.add_row(['2', '1.382432056116166e-16', '1.6033480990702738e-14 ' , '324.3452969109414'])
t.add_row(['3', '0.08888716077426202', '125.52618502073297' , '1979.784238115514 '])
t.add_row(['4', '0.11662253202502817 ', '3071.964273094497' , '93274.94345488884 '])
t.add_row(['5', '0.09923406605142177 ', '9.289402799462197e+28 ' , '1.0372867799233842e+31'])
    
print t
