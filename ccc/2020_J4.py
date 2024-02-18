t = input()
s = input()

found = "no"
for i in range(len(s)):
    s = s[1:] + s[0]
    if s in t:
        found = "yes"

print(found)