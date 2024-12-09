n = int(input())
l = [int(x) for x in input().split()]
g = [0]*n
for i in range(n):
    g[l[i]-1]=i+1
for j in g:
    print(j)

