import sys

c = int(sys.stdin.readline())
b = int(sys.stdin.readline())

computers = [False] * (c + 1)
computers[1] = True
graph=[]
for _ in range(b):
    n1, n2 = map(int, sys.stdin.readline().split(' '))
    graph.append([n1, n2])

for i in range(b):
    x, y = graph[i]
    if computers[x] or computers[y]:
        computers[x], computers[y] = True, True

cnt = 0
for c in computers:
    if c:
        cnt += 1
print(cnt - 1)