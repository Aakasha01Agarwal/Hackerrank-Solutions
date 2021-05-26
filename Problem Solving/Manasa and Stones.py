for _ in range(int(input())):
    n= int(input())
    a,b = sorted([int(input()), int(input())])
    print(*range((n-1)*a, (n-1)*b+1, b-a or 1))
