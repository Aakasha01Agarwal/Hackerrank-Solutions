def diagonalDifference(arr):
    n=len(arr)
    right_diag=[]
    left_diagonal=[]

    
    arr_=[item for val in arr for item in val ]
    
    for i in range(n):
        for j in range(n):
            if i==j:
                right_diag.append(1)
            else:
                right_diag.append(0)
    for i in range(n):
            for j in range(n):
                if (i+j)==n-1:
                    left_diagonal.append(1)
                else:
                    left_diagonal.append(0)
    

    right=[]
    for i in range(n*n):
        right.append(right_diag[i]*arr_[i])

    left=[]
    for i in range(n*n):
        left.append(left_diagonal[i]*arr_[i])
    

    result=abs(sum(right)-sum(left))
    return result
   
