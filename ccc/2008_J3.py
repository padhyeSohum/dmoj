from math import ceil

grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '-', '.', 'enter']

waypoint = list(input())
curr_row = 1
curr_col = 1
movement = 0

for i in range(len(waypoint)):
    next_row = (ceil((grid.index(waypoint[i])+1)/6))
    next_col = ((grid.index(waypoint[i])+1)%6)

    movement += abs(next_row - curr_row) + abs(next_col - curr_col)

    curr_row = next_row
    curr_col = next_col

movement += abs(6 - curr_col) + abs(5 - curr_row)

print(movement)