a = [list(map(int,input().split())) for _ in range(5)]
m = 0
n = 0
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            m=i+1
            n=j+1
            break
#break did the magic
print(abs(3-m)+abs(3-n))