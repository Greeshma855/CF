n = int(input())
c = 0
for i in range(0,n):
    l = (input().split(" "))
    l = [int(x) for x in l]
    if((l[0]==1 and l[1]==1 and l[2]==0) or (l[0]==1 and l[1]==0 and l[2]==1) or (l[0]==0 and l[1]==1 and l[2]==1) or (l[0]==1 and l[1]==1 and l[2]==1)):
        c+=1
print(c)
