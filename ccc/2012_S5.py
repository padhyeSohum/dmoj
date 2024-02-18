r, c = (int(x) for x in input().split())

grid = []
for i in range(r):
    grid.append([])
    for j in range(c):
        grid[i].append([])


k = int(input())
for i in range(k):
    cat_r, cat_c = (int(x)-1 for x in input().split())
    grid[cat_r][cat_c] = 0

unreachable = False
for i in range(c):
    if grid[0][i] == 0:
        unreachable = True
    if unreachable == True:
        grid[0][i] = 0
    else:
        grid[0][i] = 1

unreachable = False
for i in range(r):
    if grid[i][0] == 0:
        unreachable = True
    if unreachable == True:
        grid[i][0] = 0
    else:
        grid[i][0] = 1

for i in range(1,r):
    for j in range(1,c):
        if grid[i][j] == 0:
            continue
        
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid[r-1][c-1])