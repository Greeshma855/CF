t = int(input())
y = []
for i in range(t):
    l,r,k=[int(x) for x in input().split()]
    c = 0
    u = r // k
    if l>u:
        c = 0
    else:
        # works even without min only by taking u
        c=min(r, u) - l + 1
    y.append(c)
for i in y:
    print(i)



#taken out as taking lot of space for higher values
# s = list(range(l,r+1))


#2nd 8th is taking time    
# for j in s:
    #     if (r//j)>=k:
    #         c+=1

#1st 7th is also taking time
    # for j in s:
    #     u=0
    #     for z in s:
    #         if z%j==0:
    #             u+=1
    #     if u>=k:
    #         c+=1