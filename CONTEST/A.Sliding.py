t = int(input())
r = []

for _ in range(t):
    n, m, x, y = map(int, input().split())
    
    # Calculate position in grid
    pos = (x-1) * m + y
    total = n * m
    
    # Calculate remaining positions
    remaining = total - pos
    
    # Calculate number of complete rows and remaining cells in last row
    complete_rows = remaining // m
    last_row_cells = remaining % m
    
    # Calculate distance
    s = 0
    
    # Distance for complete rows (moving right then down)
    if complete_rows > 0:
        s += (m-1) * complete_rows  # horizontal moves in complete rows
        s += complete_rows          # vertical moves between rows
    
    # Distance for last row cells
    if last_row_cells > 0:
        s += last_row_cells - 1
    
    r.append(s)

print(*r, sep="\n")










# t = int(input())
# r = []

# for _ in range(t):
#     k = input()
#     l = [int(x) for x in k.split()]
#     # rows, cols = l[0], l[1]
#     # start_row, start_col = l[2], l[3]
#     s = 0
#     start_pos = (l[2] - 1) * l[1] + (l[3] - 1)
#     total_cells = l[0] * l[1]
#     curr_pos = start_pos + 1
#     while curr_pos < total_cells:
#         prev_row = ((curr_pos - 1) // l[1]) + 1
#         prev_col = ((curr_pos - 1) % l[1]) + 1
#         curr_row = (curr_pos // l[1]) + 1
#         curr_col = (curr_pos % l[1]) + 1
#         s += abs(curr_row - prev_row) + abs(curr_col - prev_col)
#         curr_pos += 1
#     r.append(s)
# print(*r, sep="\n")















# t = int(input())
# s = 0
# r = []
# for i in range(t):
#     k = input()
#     l = [int(x) for x in k.split()]
#     a = []
#     for j in range(l[0]):
#          for k in range(l[1]):
#             a.append([j+1,k+1])
#     z = a.index([l[2],l[3]])
#     for j in range(z+1,(l[0]*l[1])):
#         s+= (abs(a[j][0]-a[j-1][0])+abs(a[j][1]-a[j-1][1]))
#     r.append(s)
# print(*r, sep="\n")










