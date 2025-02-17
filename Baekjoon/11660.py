import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0]+list(map(int, input().split())) for _ in range(n)]
board.insert(0, [0 for _ in range(n+1)])

for i in range(n+1):
    for j in range(1, n+1):
        board[i][j] = board[i][j] + board[i][j-1]
    if i >= 1:
        for j in range(1, n+1):
            board[i][j] += board[i-1][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = board[x2][y2]-\
                board[x2][y1-1]-\
                board[x1-1][y2]+\
                board[x1-1][y1-1]
    
    print(result)