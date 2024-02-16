q = int(input())
n = int(input())
dmojistan = input()
pegland = input()

dmojistan = list(dmojistan.split(' '))
pegland = list(pegland.split(' '))

for i in range(n):
    dmojistan[i] = int(dmojistan[i])
    pegland[i] = int(pegland[i])

n_total = 0

dmojistan.sort()
pegland.sort(reverse=(q==2))

for i in range(n):
    n_total += max(dmojistan[i], pegland[i])

print(n_total)