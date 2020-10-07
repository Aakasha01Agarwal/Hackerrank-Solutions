import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height=1
    s=0


    if n==0:
        return(1)

    else:

        for i in range(1,n+1):
            if i%2==0:
                height+=1
                
            elif i%2==1:
                height=2*height
        return(height)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()