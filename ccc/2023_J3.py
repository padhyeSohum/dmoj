n = int(input())

availability = []
max_n = 0
days_max = []

for i in range(n):
    availability.append(input())

for i in range(len(availability[0])):
    y = 0
    for j in range(len(availability)):
        if availability[j][i] == 'Y':
            y += 1
    
    if y > max_n:
        max_n = y
        days_max = [str(i+1)]
    elif y == max_n:
        days_max.append(str(i+1))

print(','.join(days_max))