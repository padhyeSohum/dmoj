playlist = ["A", "B", "C", "D", "E"]

button = 0
while button != 4:
    button = int(input())
    n = int(input())

    if button == 1:
        for i in range(n):
            playlist = playlist[1:5] + [playlist[0]]
    elif button == 2:
        for i in range(n):
            playlist = [playlist[-1]] + playlist[0:4]
    elif button == 3:
        for i in range(n):
            playlist = [playlist[1], playlist[0]] + playlist[2:5]

print(" ".join(playlist))