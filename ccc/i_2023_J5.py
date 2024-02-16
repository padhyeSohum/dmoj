word = input()
rows = int(input())
columns = int(input())
grid = []
count = 0

for i in range(rows):
    grid.append(input())

for i in range(rows):
    # first letter detected
    for j in range(columns):
        around = [[-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0]] #starting from top left going clockwise
        if word[0] == grid[i][j]:
            if i == 0:
                around[0] = '0'
                around[1] = '0'
                around[2] = '0'
            elif i == rows - 1:
                around[4] = '0'
                around[5] = '0'
                around[6] = '0'
            if j == 0:
                around[6] = '0'
                around[7] = '0'
                around[0] = '0'
            if j == columns - 1:
                around[2] = '0'
                around[3] = '0'
                around[4] = '0'
        
        for k in range(len(around)):
            if around[k] != '0':
                if grid[j][i] == word[1]:
                    print('cool')

            
        # check if second letter is in any of the surrounding cells
    # if it is, then check if that direction has enough space for the rest of the word
    # if enough space, make a for loop with the length of the word that steps in that direction to see if each letter matches with the word
    # if every letter matches, then 

print(count)