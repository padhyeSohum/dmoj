from math import floor, sqrt

perfect_numbers = []

for i in range(1000, 10000):
    divisor_sum = 0
    for j in range(1,floor(sqrt(i))):
        if i % j == 0:
            divisor_sum += i/j + j

    divisor_sum -= i
    if divisor_sum == i:
        perfect_numbers.append(str(i))

print(" ".join(perfect_numbers))

cube_sums = []
for i in range(100, 1000):
    cube_sum = 0
    for j in range(len(str(i))):
        cube_sum += int(str(i)[j])**3

    if cube_sum == i:
        cube_sums.append(str(i))

print(" ".join(cube_sums))