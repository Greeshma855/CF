# t = int(input())
# r = []
# for i in range(t):
#     n,a,b = [int(z) for z in input().split()]
#     x = 0
#     y = 0
#     k = True
#     m = 0
#     s = input()
#     # print(s)
#     while (k==True and x<=a and y<=b and m<=10):
#         for j in s:
#             if j=="N":
#                 y+=1
#             elif j=="S":
#                 y-=1
#             elif j=="E":
#                 x+=1
#             elif j=="W":
#                 x-=1
#             # print(x,y)
#             if a==x and y==b:
#                 r.append("YES")
#                 n = 0
#                 k=False
#                 break
#             if x<0 or y<0:
#                 k=False
#         m+=1

#     if n!=0:
#         r.append("NO")
# for i in r:
#     print(i)
