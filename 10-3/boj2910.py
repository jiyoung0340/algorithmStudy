import sys

n, c = map(int, sys.stdin.readline().split(' '))
numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))

result = dict()

for n in numbers:
    if n in result:
        result[n] += 1
    else:
        result[n] = 1


result = sorted(result.items(), key=lambda x : x[1], reverse=True)

for r in result:
    for _ in range(r[1]):
        print(r[0], end=" ")