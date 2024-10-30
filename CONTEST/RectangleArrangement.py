t = int(input())
a = []
for i in range(t):
    n = int(input())
    q = []
    w=0
    h=0
    for j in range(n):
        k = input()
        l = [int(x) for x in k.split()]
        if l[0]>w:
            w=l[0]
        if l[1]>h:
            h=l[1]
        q.append(l)
    a.append((w+h)*2)


for i in a:
    print(i)