n = int(input())
cap = 0 
t = 0
for i in range(n):
    a,b=[int(x) for x in input().split()]
    t = t-a+b
    if (t>cap):
        cap=(t)
if(t==0):
    print(cap)
    