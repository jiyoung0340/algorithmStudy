import sys

n, k = map(int, sys.stdin.readline().split(' '))
coins = []
count = 0
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort(reverse=True)

for i in range(len(coins)):
    count += (k // coins[i])
    k = k % coins[i]

print(count)