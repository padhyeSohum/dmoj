t = input()

max_len = 1
for i in range(len(t)):
    for j in range(i+1, len(t)):
        checked_str = t[i:j+1]
        if checked_str == checked_str[::-1] and len(checked_str) > max_len:
            max_len = max(len(checked_str), max_len)

print(max_len)