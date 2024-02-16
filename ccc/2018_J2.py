n = int(input())
d1 = input()
d2 = input()
result = 0

for i in range(n):
    if d1[i] == "C" and d1[i] == d2[i]:
        result += 1

print(result)