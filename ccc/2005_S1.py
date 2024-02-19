t = int(input())

numbers = []
for i in range(t):
    number = input().replace("-", "")
    number = number[0:min(len(number), 10)]
    numbers.append(number)

mappings = {2: ["A", "B", "C"], 3: ["D", "E", "F"], 4: ["G", "H", "I"], 5: ["J", "K", "L"], 6: ["M", "N", "O"], 7: ["P", "Q", "R", "S"], 8: ["T", "U", "V"], 9: ["W", "X", "Y", "Z"]}

for i in range(len(numbers)):
    for j in range(min(len(numbers[i]), 10)):
        if numbers[i][j].isalpha():
            for k in range(2,10):
                if numbers[i][j] in mappings[k]:
                    numbers[i] = numbers[i].replace(numbers[i][j], str(k))

    print(numbers[i][0:3] + "-" + numbers[i][3:6] + "-" + numbers[i][6:10])