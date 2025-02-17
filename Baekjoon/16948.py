import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

def bfs(r, c):
    q = deque([(r1, c1, 0)])
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1

    while q:
        r, c, cnt = q.popleft()

        if r == r2 and c == c2:
            return cnt
        else:
            for dx, dy in [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]:
                if -1 < r + dx < n and -1 < c + dy < n and not visited[r+dx][c+dy]:
                    q.append((r+dx, c+dy, cnt+1))
                    visited[r+dx][c+dy] = 1

    return -1

print(bfs(r1, c1))