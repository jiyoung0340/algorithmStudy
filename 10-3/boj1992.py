import sys

n = int(sys.stdin.readline())

graph = [ list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = []
def sol(s_x, s_y, n):
    for i in range(s_x, n):
        for j in range(s_y, n):
            if graph[s_x][s_y] != graph[i][j]:
                sol(s_x, s_y, int(n / 2))
                sol(s_x + int(n / 2), s_y, int(n /2))
                sol(s_x, s_y + int(n / 2), int(n /2))
                sol(s_x + int(n / 2), s_y + int(n / 2), int(n /2))
    result.append(graph[s_x][s_y])

sol(0, 0, n)
print(result)