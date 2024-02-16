n = int(input())
arr = []

for i in range(n):
    arr.append([input(), int(input())])

arr_sorted = sorted(arr, reverse=True, key=lambda x: x[1])
highest_bids = []
highest_bids.append(arr_sorted[0])

for i in range(len(arr_sorted)):
    if i == 0:
        continue
    if i < len(arr_sorted) - 2:
        if arr_sorted[i] == arr_sorted[i+1]:
            highest_bids.append(arr_sorted[i+1])

if len(highest_bids) == 1:
    print(highest_bids[0][0])
else:
    lowest = len(arr) - 1
    for i in range(len(highest_bids)):
        if arr.index(highest_bids[i]) < lowest:
            lowest = arr.index(highest_bids[i])
    
    print(arr[lowest][0])