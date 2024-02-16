n = int(input())

row_1 = input().split(' ')
row_2 = input().split(' ')

tape_needed = 0

for i in range(len(row_1)):
    if row_1[i] == '1':
        if i == 0:
            tape_needed += 3
        else:
            tape_needed += 3 - (2 if row_1[i-1] == '1' else 0)

for i in range(len(row_2)):
    if row_2[i] == '1':
        if i == 0:
            tape_needed += 3 - (2 if row_1[0] == '1' else 0)
        else:
            tape_needed += 3 - (2 if row_2[i-1] == '1' else 0) - (2 if i % 2 == 0 and row_1[i] == '1' else 0)

print(tape_needed)