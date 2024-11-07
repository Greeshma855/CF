t = int(input())
a = []
for i in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    s = sum(l)
    off = 0
    on = 0
    for j in l:
        if j==0:
            off+=1
        elif j==1:
            on+=1
    if on<=n:
        max=on
    else:
        # max=on%2
        max = off
    min=on%2
    a.append([min,max])
    # if s<=n:
    #     max=s
    # else:
    #     max=0
    # if max<s%2:
    #     max=s%2
    # a.append([s%2,max])
for k in a:
    print(k[0], k[1])
