n,k = (input().split())
n = int(n)
k = int(k)
l = (input().split())
l = [int(x) for x in l]
m = l[k-1]
print(m)
c = 0
for i in range(0,n):
    if l[i]==m and m>0:
        c=i+1
if m<=0:
    print("entered")
    for j in range(k-2,0):
        if l[j]<=0:
            print("ye")
            c=j
            break
print(c)
