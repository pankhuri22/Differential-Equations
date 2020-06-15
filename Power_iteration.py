import numpy as np
def Power_itr(A,vo): 
    
    count = 0 
    while(True): 
         
        initial = np.dot(A,vo) 
        norm = np.linalg.norm(initial,np.inf) 
        X = initial / norm
        count =count + 1 

        if count > 100: 
            break      
        vo = X 
    return norm,vo


A = np.array([[2,3,2],[10,3,4],[3,6,1]])
vo = np.array([0,0,1])
c = Power_itr(A,vo)
print c