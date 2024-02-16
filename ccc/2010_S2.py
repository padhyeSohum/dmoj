k = int(input())

chars = {}
for i in range(k):
    line = input().split(' ')
    chars[line[1]] = line[0]

input_string = input()

checked_string = ""
result_string = ""

for i in range(len(input_string)):
    checked_string += input_string[i]
    if checked_string in chars:
        result_string += chars[checked_string]
        checked_string = ""

print(result_string)