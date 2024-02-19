rotatable = True
for i in input():
    if i not in ["I", "O", "S", "H", "Z", "X", "N"]:
        rotatable = False
        break

print("YES") if rotatable else print("NO")