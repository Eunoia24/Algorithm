import sys

n = int(input())
region = [list(map(int, input().split())) for _ in range(n)]

max_value = 0
def bfs(pos, visited):
    q = [(pos)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        cur_pos = q.pop()
        for i in move:
            y, x = cur_pos[0] + i[0], cur_pos[1] + i[1]
            if 0 <= y < n and 0 <= x < n:
                if visited[y][x] == 0:
                    visited[y][x] = 1
                    q.append((y, x))

for i in range(max(max([max(i) for i in region]), 101)):
    cnt = 0
    # 물에 잠긴 지역 1, 잠기지 않은 지역 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if region[j][k] <= i:
                visited[j][k] = 1

    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0:
                bfs((j, k), visited)
                cnt += 1

    if cnt > max_value:
        max_value = cnt

print(max_value)