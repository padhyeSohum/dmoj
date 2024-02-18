y = int(input()) + 1

def countDistinct(num):
    num_list = list(str(num))
    num_list.sort()

    count = 1
    for i in range(1,len(num_list)):
        if num_list[i] != num_list[i-1]:
            count += 1
    
    return(count)

while countDistinct(y) != len(str(y)):
    y += 1

print(y)