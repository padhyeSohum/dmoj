aromatic = input()
values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
aromatic_list = []
result = 0

i = 0
while i < len(aromatic):
    aromatic_list.append([int(aromatic[i]), values[aromatic[i+1]]])
    i += 2

for i in range(len(aromatic_list)):
    if i == 0:
        result += aromatic_list[i][0] * aromatic_list[i][1]
    elif aromatic_list[i][1] > aromatic_list[i-1][1]:
        result += aromatic_list[i][0]*aromatic_list[i][1] - 2*aromatic_list[i-1][0]*aromatic_list[i-1][1]
    else:
        result += aromatic_list[i][0]*aromatic_list[i][1]

print(result)