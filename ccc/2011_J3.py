prev = int(input())
curr = int(input())
length = 2

while prev >= curr:
    temp = curr
    curr = prev - curr
    prev = temp
    length += 1

print(length)