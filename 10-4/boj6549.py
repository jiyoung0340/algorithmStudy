import sys

while(True):
    rect_list = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    n = rect_list[0]
    area = 0
    if n == 0:
        break
    else:
        rect_list = rect_list[1:len(rect_list)]
        area = rect_list[0]
        for i in range(n):
            for j in range(i + 1, n):
                rect_range = rect_list[i:j]
                wh = min(rect_range) * (j - i + 1)
                area = max(wh, area)
        print(area)

