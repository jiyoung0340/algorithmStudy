import sys
import itertools


while(True):
    test = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if len(test) == 1 and test[0] == 0:
        break
    else:
        k = test[0]
        s = test[1:]
        res = itertools.combinations(s, 6)
        for r in res:
            for e in r:
                print(e, end=" ")
            print("")
    print("")


