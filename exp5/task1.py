import numpy as np

def even_parity(seq):
    sum = None
    for d in seq: 
        if sum == None:
            sum = d
        else:
            sum = sum ^ d
    
    return False if sum else True
     
def rect_parity(codeword, nrows, ncols):
    
    data_bits_len = nrows*ncols
    data_bits = codeword[:data_bits_len].reshape((nrows,ncols))
    
    R = codeword[data_bits_len:data_bits_len+nrows].tolist()
    C = codeword[data_bits_len+nrows:data_bits_len+nrows+ncols].tolist()
    
    print('Databits: ')
    print(data_bits)
    
    row_sum = []
    for row in data_bits:
        if even_parity(row):
            row_sum.append(0)
        else:
            row_sum.append(1)
    
    column_sum = []
    for row in data_bits.transpose():
        if even_parity(row):
            column_sum.append(0)
        else:
            column_sum.append(1)

    print('Row Sum: ',row_sum)
    print('Column Sum: ',column_sum)
    
    print('Row parity bits: ',R)
    print('Column parity bits: ',C)
    
    row_error = 0
    column_error = 0
    row_index = 0
    column_index = 0
    for i in range(nrows):
        if row_sum[i] != R[i]:
            print("Parity error in row {}".format(i+1))
            row_error += 1
            row_index = i
    
    for i in range(ncols):
        if column_sum[i] != C[i]:
            print("Parity error in column {}".format(i+1))
            column_error += 1
            column_index = i
    
    message_sequence = data_bits

    if row_error == 1 and column_error == 1:
    	message_sequence[row_index,column_index] = not(data_bits[row_index,column_index])
    elif row_error == 0 and column_error == 0:
    	print('No correction is necessary')
    elif row_error == 1 or column_error == 1:
    	print('Error detected in parity bits, hence no change in data bits')
    else:
    	print('Uncorrectable error is detected')
        
    return message_sequence

def test_correct_errors():        
    nrows = 2
    ncols = 4
    codeword1 = np.array( [0, 1, 1, 0, 1, 1, 0, 1,
                        0,1, 
                        1, 0, 1, 1] )
    codeword2 = np.array( [1, 0, 0, 1, 0, 0, 1, 0,
                        1,1, 
                        1, 0, 1, 0] )  
    codeword3 = np.array( [0, 1, 1, 1, 1, 1, 1, 0,
                        1,1, 
                        1, 0, 0, 0] )  
    print('Codeword 1')
    message_sequence = rect_parity(codeword1,nrows,ncols)
    print('Message Sequence: ')
    print(message_sequence)
    print('\nCodeword 2')
    message_sequence = rect_parity(codeword2,nrows,ncols)
    print('Message Sequence: ')
    print(message_sequence)
    print('\nCodeword 3')
    message_sequence = rect_parity(codeword3,nrows,ncols)
    print('Message Sequence: ')
    print(message_sequence)


if __name__ == "__main__":
    test_correct_errors()
    


        
        
    
