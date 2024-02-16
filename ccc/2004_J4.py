alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

key = list(input())
message = list(input())
fixed_message = [c for c in message if c.isalpha()]

message = fixed_message

for i in range(len(key) - (len(message) % len(key))):
    message.append(' ')

grid = [[]]

for i in range(len(key)):
    grid[0].append(alphabet.index(key[i]))

for i in range(len(message)//len(key)):
    grid.append(message[i*len(key):i*len(key)+len(key)])

for i in range(len(message)):
    curr = message[i]
    if curr != ' ':
        grid[i//len(key) + 1][i%len(key)] = alphabet[(alphabet.index(curr) + grid[0][i%len(key)]) % len(alphabet)]

encoded_message = ""
for i in range(len(grid) - 1):
    encoded_message += ''.join(grid[i+1])

print(encoded_message.rstrip())