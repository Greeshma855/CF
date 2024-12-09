n,h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
c = 0
for i in a:
    if i>h:
        c+=2
    else:
        c+=1
print(c)