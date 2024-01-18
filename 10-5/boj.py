import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

# 최소신장트리알고리즘
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는가
#     2-1. 사이클이 발생 안하면 최소 신장 트리에 포함
#     2-2. 사이클이 발생 하면 포함안함
# 3. 2번 과정을 모든 간선에 대해 반복

# 위상 정렬 : 방향성이 있고 사이클이 없는 그래프에서 그 방향을 거스르지않고 순서대로 나열하는 것
# 1. 진입차수가 0인 모든 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#     2-1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
#     2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# 각 노 드가 큐에 들어온 순서가 위상 정렬한 결과

# 우선순위 큐
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
res = heapsort(arr)
for i in range(n):
    print(res[i])

