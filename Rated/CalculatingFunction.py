t = int(input())
if t%2==0:
    n=m=t//2
else:
    m = t//2
    n = t//2+1
e = n*(n+1)/2
o = m*m
print(o-e)