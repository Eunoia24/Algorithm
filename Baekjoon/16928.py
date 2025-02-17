import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
ladders = [tuple(map(int, input().split())) for _ in range(N)]
snakes = [tuple(map(int, input().split())) for _ in range(M)]

visited = [0 for _ in range(101)]
visited[1] = 1

def check(pos):
    global ladders, snakes, visited
    visited[pos] = 1

    for i in range(len(ladders)):
        if ladders[i][0] == pos:
            visited[ladders[i][1]] = 1
            return ladders[i][1]
    for i in range(len(snakes)):
        if snakes[i][0] == pos:
            visited[snakes[i][1]] = 1
            return snakes[i][1]
    return pos


def bfs():
    global ladders, snakes
    q = deque([[1, 0]])

    while q:
        cur, cnt = q.popleft()

        if cur >= 100:
            return cnt
        else:
            for dd in range(1, 7):
                if cur + dd >= 100:
                    return cnt + 1
                elif not visited[cur + dd]:
                    q.append([check(cur + dd), cnt + 1])

print(bfs())