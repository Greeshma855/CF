t = int(input())
l = []
for i in range(t):
    n = [int(x) for x in input()]
    s = sum(n)
    tw = n.count(2)    #count no.of 2's
    th = n.count(3) 
    # print(s)   #count no.of 3's
    # print(tw)
    # print(th)    
    r = s%9
    # print(r)
    z = 0
    if r==0:
        z = 1
    elif r==1 and (tw>=4 or (tw>=1 and th>=1)):
        z = 1
    elif r == 8 and (tw>=5 or (tw>=2 and th>=1)):
        z = 1
    elif r==7 and tw>=1:
        z =1
    elif r==6 and (tw>=6 or th>=2):
        z = 1
    elif r==5 and tw>=2:
        z = 1
    elif r==4 and (tw>=7 or (tw>=1 and th>=2) or (tw>=4 and th>=1)):
        z = 1
    elif r==3 and (th>=1 or tw>=3):
        z = 1
    elif r==2 and (tw>=8 or (tw>=2 and th>=2) or (tw>=5 and th>=1)):
        z = 1
    if z==1:
        l.append("YES")
        # print("YES")
    else:
        l.append("NO")
        # print("NO")
for i in l:
    print(i)





#     if r==0:
#         z = 1
#     elif r==1 and (tw>=5 or (tw>=2 and th>=2)):
#         z = 1
#     elif r == 7 and tw>=1:
#         z = 1
#     elif r==6 and th>=1:
#         z =1
#     elif r==5 and tw>=2:
#         z = 1
#     elif r==4 and tw>=1 and th>=1:
#         z = 1
#     elif r==3 and (tw>=3 or th>=2):
#         z = 1
#     elif r==2 and tw>=2 and th>=1:
#         z = 1
#     elif r==8 and (tw>=4 or (tw>=1 and th>=2)):
#         z = 1
#     if z==1:
#         l.append("YES")
#         # print("YES")
#     else:
#         l.append("NO")
#         # print("NO")
# for i in l:
#     print(i)
    # 10 - 2,2,2,2,2 or 3,3,2,2 
    # 2 - 2
    # 3 - 3
    # 4 - 2,2
    # 5 - 2,3
    # 6 - 2,2,2 or 3,3
    # 7 - 2,2,3
    # 8 - 2,2,2,2 or 3,3,2



    # 2 - 4(add 2)
    # 3 - 9(add 6)













    # n = [int(x) for x in input()]
    # for i in range(len(n)):
    #     if n[i]*n[i]<=9:
    #         n[i]=n[i]*n[i]
    #     s = sum(n)
    #     if (s//9) == 0:
    #         print("YES")
    #         # break
    #     else:
    #         print(n)
    #         print("NO")
