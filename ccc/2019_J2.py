l = int(input())

for i in range(l):
    line = input().split(" ")
    line[0] = int(line[0])

    print(line[0]*line[1])