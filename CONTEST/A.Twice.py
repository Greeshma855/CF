t = int(input())
z = []
for i in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    c = 0
    u = [False]* len(l)
    for j in range(len(l)):
        if u[j]:
            continue
        for k in range(j+1,len(l)):
            if l[j]==l[k] and not u[k]:
                u[j]=True
                u[k]=True
                c+=1
                break
    z.append(c)
for i in z:
    print(i)
