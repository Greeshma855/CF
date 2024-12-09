t = int(input())
l = []
for i in range(t):
    n,m = [int(x) for x in input().split()]
    c = 0
    w = 0
    for j in range(n):
        x = input()
        c+=len(x)
        if c<=m:
            w+=1
    l.append(w)

for i in l:
    print(i)

