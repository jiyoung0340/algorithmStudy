import sys

t = int(sys.stdin.readline())


def change_numbers(numbers, change):
    global res

    num = ''
    for number in numbers:
        num += number

    if int(num) in res:
        return
    else:
        res[change].append(int(num))

    if change == 0:
        return

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            change_numbers(numbers, change - 1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


for i in range(1, t+1):
    numbers, change = sys.stdin.readline().split(' ')
    numbers = list(numbers)
    res = [[] for _ in range(int(change) + 1)] # 교환 횟수 마다 변화되는 값 - 나중에 result[0]에서 max값을 찾는다.
    change_numbers(numbers, int(change))
    print("#",i," ",max(res[0]), sep="")