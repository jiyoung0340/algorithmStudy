import math
from itertools import permutations

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    numbers_list = list(map(int,numbers))
    result_list = []

    for i in range(1, len(numbers_list) + 1): # 자릿수
        result_list.extend(list(permutations(numbers_list, i)))

    int_list= []
    # for num in result_list:
        # 조합을 int 숫자로 변환...

    print(int_list)
    return answer


numbers = "011"
print(solution(numbers))
