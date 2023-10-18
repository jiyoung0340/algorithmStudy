from collections import deque

def compare_word(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)
    cnt = 0
    for i in range(len(word1_list)):
        if word2_list[i] != word1_list[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    q = deque()

    q.append([begin, 0])
    while q:
        begin_word, cnt = q.popleft()
        if begin_word == target:
            answer = cnt
            break
        for word in words:
            if compare_word(begin_word, word):
                q.append([word, cnt + 1])
    return answer


begin = "hit"
target = "cog"
words =["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words))