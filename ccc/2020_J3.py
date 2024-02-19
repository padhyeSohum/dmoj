n = int(input())

coords = []
for i in range(n):
    x, y = input().split(",")
    coords.append([int(x), int(y)])

sorted_x = sorted(coords)
sorted_y = sorted(coords, key=lambda x: x[1])

print(f"{sorted_x[0][0]-1},{sorted_y[0][1]-1}")
print(f"{sorted_x[-1][0]+1},{sorted_y[-1][1]+1}")