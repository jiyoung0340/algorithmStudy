import sys

n = int(sys.stdin.readline())
move = list(sys.stdin.readline().split(' '))
# L : (-1, 0)
# R : (1, 0)
# U : (0, -1)
# D : (0, 1)
now= [1, 1]

for m in move:
    if m == "L":
        if now[1] > 1:
            now[1] -= 1
    elif m == "R":
        if now[1] < n:
            now[1] += 1
    elif m == "U":
        if now[0] > 1:
            now[0] -= 1
    else:
        if now[0] < n:
            now[0] += 1

print(now[0], now[1])
