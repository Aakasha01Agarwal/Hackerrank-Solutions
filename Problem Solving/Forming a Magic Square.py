import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    s=[ item for elem in s for item in elem]
    # print(s)
    all_n = [
                [8, 1, 6, 3, 5, 7, 4, 9, 2],
                [6, 1, 8, 7, 5, 3, 2, 9, 4],
                [4, 9, 2, 3, 5, 7, 8, 1, 6],
                [2, 9, 4, 7, 5, 3, 6, 1, 8],
                [8, 3, 4, 1, 5, 9, 6, 7, 2],
                [4, 3, 8, 9, 5, 1, 2, 7, 6],
                [6, 7, 2, 1, 5, 9, 8, 3, 4],
                [2, 7, 6, 9, 5, 1, 4, 3, 8]
            ]
 
    cost = []
    for i in range(8):
        sum=0
        for j in range(9):
            
            c=abs(all_n[i][j]-s[j])
            sum+=c
            # print("This is BLOCK NUMBER ", i)
            # print(c)
        
        cost.append(sum)
        # print(cost[i])
        
    return (min(cost))

        
 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()