n = int(input())
cnt = 0
while(n>0):
    x =  n%10
    if x==4 or x==7:
        cnt+=1
    n = n//10
if(cnt==4 or cnt==7):
    print("YES")
else:
    print("NO")