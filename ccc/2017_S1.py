n = int(input())

swifts = input().split(' ')
swifts = [ int(x) for x in swifts ]

semaphores = input().split(' ')
semaphores = [ int(x) for x in semaphores ]

total_swifts = 0
total_semaphores = 0

k = 0

for i in range(n):
    total_swifts += swifts[i]
    total_semaphores += semaphores[i]

    if total_swifts == total_semaphores:
        k = i+1

print(k)