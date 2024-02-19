n = int(input())

pos_times = []

for i in range(n):
    time, position = input().split()
    pos_times.append([int(time), int(position)])

pos_times.sort()

max_speed = 0

for i in range(1,len(pos_times)):
    max_speed = max(max_speed, abs(pos_times[i][1]-pos_times[i-1][1])/(pos_times[i][0]-pos_times[i-1][0]))

print(max_speed)