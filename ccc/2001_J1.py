h = int(input())

for i in range(h):
    row = i
    num_asterisks = min(2*row+1, 2*(h-row)-1)
    print('*'*num_asterisks + ' '*(2*h-2*num_asterisks) + '*'*num_asterisks)