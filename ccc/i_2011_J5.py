n = int(input())
total = 2

network = []
for i in range(n-1):
    network.append([int(input()), i+1])

print(network)

# for i in range(n-1):
#     for j in range(n-1):
#         if i+1 == network[j][1]:
#             for k in range(n-1):
#                 if j != k:
#                     if i+1 == network[k][0]:


# check = []
# for i in range(len(network)):
#     if network[i][1] not in check:
#         check.append(i+1)
#     else:
#         if network[i][0] in

# dict = {
#     "1": [],
#     "2": [],
#     "3": [],
#     "3": [],
#     "5": [],
#     "6": []
# }

# for i in range(len(network)):
#     dict[network[i][0]-1].append(network[i][1])

# print(dict)