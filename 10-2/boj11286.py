import sys
import heapq

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if numbers:
            print(heapq.heappop(numbers)[1])
        else:
            print(0)
    else:
        heapq.heappush(numbers, (abs(num), num))


