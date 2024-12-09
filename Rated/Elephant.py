x = int(input())
s = 0
s = s+(x//5)
x = x%5
s = s+(x//4)
x = x%4
s = s+(x//3)
x = x%3
s = s+(x//2)
x = x%2
s = s+(x//1)
x = x%1
print(int(s))