import sys

n = sys.stdin.readline()
m = int(sys.stdin.readline())
broken_number = list(map(int, sys.stdin.readline().rstrip().split(' ')))

cnt = 0

def find_n(now):
    global cnt

    if now == int(n):
        return cnt
    else:
