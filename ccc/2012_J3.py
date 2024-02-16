grid = [['*', 'x', '*'], [' ', 'x', 'x'], ['*', ' ', '*']]
k = int(input())

line_to_print = ""
for i in range(len(grid)):
    for j in range(len(grid[0])):
        line_to_print += grid[i][j]*k
    for l in range(k):
        print(line_to_print)
    
    line_to_print = ""