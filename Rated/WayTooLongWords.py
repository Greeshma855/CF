n = int(input())
a = []
for i in range(0,n):
    l = input()
    if len(l)>10:
        l=l[0]+str(len(l)-2)+l[len(l)-1]
    a.append(l)
for j in a:
    print(j)