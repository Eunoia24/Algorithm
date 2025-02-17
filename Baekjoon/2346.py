from collections import deque
n = int(input())
d = deque(enumerate(map(int, input().split()), start=1))

for i in range(len(d)):
    cur = d.popleft()
    print(cur[0], end=' ')
    if cur[1] > 0:
        d.rotate(-(cur[1]-1))
    else:
        d.rotate(-cur[1])