n= int(input())
arr= list(map(int, input().split()))
c=0
def f(arr):
    c=0
    for i in range(len(arr)):
        try:
            if arr[i]%2 == 1:
                c+=2
                arr[i+1]+=1
        except:
            return('NO')
    return(c)

print(f(arr))
