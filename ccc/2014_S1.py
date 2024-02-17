k = int(input())
m = int(input())

r = []
for i in range(m):
    r.append(int(input()))

invitees = [x + 1 for x in range(k)]

for i in range(m):
    count = 0
    for j in range(len(invitees)):
        count += 1 if invitees[j] != 0 else 0
        if count == r[i]:
            invitees[j] = 0
            count = 0

remaining_invitees = [str(x) for x in invitees if x != 0]
print("\n".join(remaining_invitees))