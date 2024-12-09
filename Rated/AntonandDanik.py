i = int(input())
s = input()
a=0
d=0
for k in range(i):
    if s[k]=="A":
        a+=1
    elif s[k]=="D":
        d+=1
if(a>d):
    print("Anton")
elif(d>a):
    print("Danik")
else:
    print("Friendship")
