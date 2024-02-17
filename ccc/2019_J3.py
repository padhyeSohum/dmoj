n = int(input())

lines = [input() for x in range(n)]

for i in range(len(lines)):
    line_to_print = ""
    count = 1
    for j in range(len(lines[i])):
        curr = lines[i][j]
        if j != 0:
            prev = lines[i][j-1]
        
            if curr == prev:
                count += 1
                if j == len(lines[i]) - 1:
                    line_to_print = line_to_print + f"{count} {prev} "
            else:
                line_to_print = line_to_print + f"{count} {prev} "
                count = 1

                if j == len(lines[i]) - 1:
                    line_to_print = line_to_print + f"{count} {curr}"
    
    print(line_to_print.rstrip())
