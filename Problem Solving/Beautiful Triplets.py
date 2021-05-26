nd=list(map(int,input().split()))
n=nd[0]
d=nd[1]

c= list(map(int,input().split()))
gc=0
for i in range(n):
    if c[i]+d in c and c[i]+2*d in c:
        gc+=1
print (gc)
