n = int(input())
p1_score = 100
p2_score = 100
rolls = []

for i in range(n):
    rolls.append(input().split())

for i in range(len(rolls)):
    roll_1 = int(rolls[i][0])
    roll_2 = int(rolls[i][1])

    if roll_1 > roll_2:
        p2_score -= roll_1
    elif roll_1 < roll_2:
        p1_score -= roll_2

print(p1_score)
print(p2_score)