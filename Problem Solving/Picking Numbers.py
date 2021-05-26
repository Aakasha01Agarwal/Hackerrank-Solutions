n=int(input())

arr=list(map(int,input().split()))

arr.sort()
x=set(arr)
count=[]
for j in x:
    counter=0
    m=arr[:]
    for i in range(len(arr)):
        m[i]-=j

    # print(m)
    for i in range(len(m)):

        if m[i]==1 or m[i]==0:
            counter+=1

    count.append(counter)
print(max(count))
