n = int(input())
alice = list(input().split(' '))
bob = list(input().split(' '))
arr = ['rock', 'paper', 'scissors']

alice_wins = 0
bob_wins = 0

for i in range(n):
    if (arr.index(alice[i]) + 3) % 3 == (arr.index(bob[i]) + 3) % 3 + 1 or arr.index(alice[i]) % 3 == arr.index(bob[i]) % 3 - 2:
        alice_wins += 1
    elif (arr.index(alice[i]) + 3) % 3 == (arr.index(bob[i]) + 3) % 3 - 1 or arr.index(alice[i]) % 3 == arr.index(bob[i]) % 3 + 2:
        bob_wins += 1

print(alice_wins, bob_wins)