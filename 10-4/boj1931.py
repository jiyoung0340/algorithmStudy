import sys

n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split(' '))
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = meetings[0][1]
for i in range(1, n):
    if meetings[i][0] >= end:
        cnt += 1
        end = meetings[i][1]

print(cnt)