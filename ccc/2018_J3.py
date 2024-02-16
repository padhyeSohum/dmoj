distances_between = input().split(' ')
distances = [0]
s = 0

for i in distances_between:
    s += int(i)
    distances.append(i)

curr_distance_i = 0

for i in range(len(distances)):
    result = ""
    curr_distance_i += int(distances[i])
    curr_distance_j = 0

    for j in range(len(distances)):
        curr_distance_j += int(distances[j])

        distance = abs(curr_distance_i - curr_distance_j)
        result += str(distance) + " "
    print(result.rstrip())