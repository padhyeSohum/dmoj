n = int(input())
k = int(input())
sum = n

for i in range(k):
    sum += 10**(i+1)*n

print(sum)