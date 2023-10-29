import sys

n = int(sys.stdin.readline())
cards = {}
for _ in range(n):
    c = int(sys.stdin.readline())
    if c in cards:
        cards[c] += 1
    else:
        cards[c] = 1

cards = sorted(cards.items(), key= lambda x: (-x[1], x[0]))
print(cards[0][0])