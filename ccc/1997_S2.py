from math import sqrt, ceil

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

for i in range(len(nums)):
    sums = []
    differences = []


    number = nums[i]
    for j in range(1, ceil(sqrt(number))):
        if number % j == 0:
            sums.append(j + number/j)
            differences.append(abs(j - number/j))
    
    for k in sums:
        if k in differences:
            is_nasty = True
            break
        else:
            is_nasty = False
    
    if is_nasty:
        print(f"{number} is nasty")
    else:
        print(f"{number} is not nasty")