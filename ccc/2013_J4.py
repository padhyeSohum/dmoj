t = int(input())
c = int(input())

chores = []
for i in range(c):
    chores.append(int(input()))

chores.sort()
sum = 0
count = 0
for i in chores:
    if sum + i <= t:
        sum += i
        count += 1
    else:
        break

print(count)