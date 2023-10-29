import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
broken_number = list(map(int, sys.stdin.readline().rstrip().split(' ')))

result = abs(100 - n) # 100번 채널부터 n번까지 +/- 버튼으로만 간 경우

for i in range(1000000): # 큰수 -> 작은수 + 작은수 -> 큰수
    for j in str(i): # 1번채널부터 n번 채널까지의 최솟값을 다 구한다!
        if j in broken_number:
            break
        if j == len(str(i)) - 1:
            result = min(result, len(str(i)) + abs(i - n))

print(result)