k = int(input())

boss_directions = []
for i in range(k):
    boss_directions.append(int(input()))

result = []

for i in range(len(boss_directions)):
    curr = boss_directions[i]
    
    if curr != 0:
        result.append(curr)
    else:
        result.pop(-1)

print(sum(result))