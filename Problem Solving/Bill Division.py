import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    b_actual=0
    for i in range(len(bill)):
        if i==k:
            continue
        b_actual+=bill[i]
    b_actual=b_actual/2
    if b_actual==b:
        print("Bon Appetit")
    else:
        print(int(b-b_actual))
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
