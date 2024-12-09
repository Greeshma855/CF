n,t = [int(x) for x in input().split()]
s = list(input())
while(t>0):
    i=0
    while(i<(n-1)):
        if s[i]=='B' and s[i+1]=='G':
            k = s[i]
            s[i]=s[i+1]
            s[i+1]=k
            i+=2
        else:
            i+=1
    t-=1
print(''.join(s))