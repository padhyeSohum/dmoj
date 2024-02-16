n = int(input())
m = int(input())

n_arr = []
m_arr = []
for i in range(n):
    n_arr.append(input())

for i in range(m):
    m_arr.append(input())

for i in range(n):
    for j in range(m):
        print(n_arr[i] + " as " + m_arr[j])