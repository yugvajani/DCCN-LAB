from task2 import syndrome_decode, mod2, equal
import numpy as np


n = 7
k = 4
G = np.array([1,0,0,0,1,1,0,
                0,1,0,0,1,0,1,
                0,0,1,0,0,1,1,
                0,0,0,1,1,1,1
                ]).reshape(k,n)
# print(G)
print("Testing all 2**k = 16 valid codewords")

for number in range(2**k):
    message = np.array(list(bin(number)[2:].zfill(k)), dtype=int).reshape(1,k)
    # print(message)
    codeword = mod2(message.dot(G))
    # print(codeword)
    decoded_message = syndrome_decode(codeword, n,k,G)
    # print(decoded_message)
    if not equal(codeword, decoded_message):
        print("Error decoding {} ... expected {} got {}".format(codeword,message,decoded_message))
        break
else:
    print("...passed")

print("Testing all n*2**k = 112 single-bit error codewords")
for number in range(2**k):
    message = np.array(list(bin(number)[2:].zfill(k)),dtype=int).reshape(1,k)
    codeword = mod2(message.dot(G))
    for i in range(len(codeword)):
        codeword[i] = not(codeword[0][i])
        decoded_message = syndrome_decode(codeword, n,k,G)
        if not equal(codeword, decoded_message):
            print("Error decoding {} ... expected {} got {}".format(codeword,message,decoded_message))
            break
        else:
            codeword[i] = not(codeword[0][i])
else:
    print("...passed")

print("All 0 and 1 error tests passed for (7,4,3) code with generator matrix G = \n",G)