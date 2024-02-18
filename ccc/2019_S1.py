directions = input()

count_h = 0
count_v = 0

for i in directions:
    if i == "H":
        count_h += 1
    elif i == "V":
        count_v += 1

flip_h = count_h % 2
flip_v = count_v % 2

ln_1 = ["1", "2"]
ln_2 = ["3", "4"]
order = [ln_1, ln_2]

if flip_h == 1:
    order.reverse()
if flip_v == 1:
    order[0].reverse()
    order[1].reverse()


print(" ".join(order[0]))
print(" ".join(order[1]))