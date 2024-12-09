n = int(input())
l = []
c = 0
for i in range(n):
    l.append(int(input()))
for i in range(n-1):
    if l[i]!=l[i+1]:
        c+=1
print(c+1)