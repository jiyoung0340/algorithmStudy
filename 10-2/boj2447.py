import sys

n = int(sys.stdin.readline())


def make_pattern(n):
    if n == 1:
        return ["*"]

    stars = make_pattern(n // 3)
    res = []

    for s in stars:
        res.append(s * 3)
    for s in stars:
        res.append(s + (" "* (n // 3) ) + s)
    for s in stars:
        res.append(s * 3)
    return res


result = make_pattern(n)
for r in result:
    print(r)
