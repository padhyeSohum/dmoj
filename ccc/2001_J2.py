x = int(input())
m = int(input())

i = 0
remainders = []
while x * i % m != 1:
    
    if x * i % m in remainders:
        print("No such integer exists.")
        break
    
    remainders.append(x * i % m)
    i += 1
else:
    print(i)