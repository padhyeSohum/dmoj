k = int(input())
original_string = input()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

result = list(original_string)

for i in range(len(original_string)):

    #s = 3p+k
    p = i+1
    s = 3*p + k

    result[i] = alphabet[(alphabet.index(original_string[i])+len(alphabet)-s)%len(alphabet)]

print(''.join(result))