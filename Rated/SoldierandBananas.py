k = input()
l = [int(x) for x in k.split()]
t = int((l[2]*(l[2]+1)/2)*l[0])
if t>l[1]:
    print(t-l[1])
else:
   print(0)