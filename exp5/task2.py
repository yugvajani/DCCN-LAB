import numpy as np

#function to calculate mod to get binary matrix
def mod2(x):
    return np.mod(x,2)

#to compare matrix    
def equal(a, b):
    return np.array_equal(a,b)

def syndrome_decode(codeword, n, k, G):
    #codeword is received message
    
    #calculate A
    A = G[0:k,k:n]
    print("Matrix A:")
    print(A)

    # calculate H
    At = A.transpose()
    I = np.identity(n-k,dtype=int)
    H = np.concatenate((At,I), axis=1)
    print("Matrix H:")
    print(H)

    #calculate c_d 
    codewordT = codeword.transpose()
    c_d = mod2(H.dot(codewordT))   #c_d is syndrome for received message
    # print(c_d)

    for i in range(k):
        #generate syndromes
        P = np.array([0,0,0,0,0,0,0])   
        P[i] = 1
        syndrome = H.dot(P.transpose())  
        # print(syndrome)
        
        #check if syndrome is equal 
        if equal(syndrome,c_d):
            codeword[i] = not(codeword[i])
            break
    return(codeword[:k])

if __name__ == "__main__":
    n=7
    k=4
    G = np.array([1,0,0,0,1,1,0,
                0,1,0,0,1,0,1,
                0,0,1,0,0,1,1,
                0,0,0,1,1,1,1
                ]).reshape(k,n)
    print("Generator Matrix:")
    print(G)  
    codeword = np.array([1,1,1,0,1,0,1])   #error at pos 2       
    message = syndrome_decode(codeword, n, k, G)
    # print(message)
    print("Received message:")  
    print(''.join(map(str,message.tolist())))
    





