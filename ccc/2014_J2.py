num_v = int(input())

votes = input()

a = 0
b = 0
for i in range(len(votes)):
    if votes[i] == "A":
        a += 1
    else:
        b += 1

print("A") if a > b else print("B") if b > a else print("Tie")