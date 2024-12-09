t = int(input())
for i in range(t):
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    s = 0
    while(s<k):
       s = max(a)
       a.remove(s)