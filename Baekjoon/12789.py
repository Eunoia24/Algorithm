from collections import deque

n = int(input())
q, s, isPrint = deque(map(int, input().split())), [], True

std = 1
while q or s:
    if q:
        cur = q.popleft()
        if cur == std:
            std += 1
        else:
            if s:
                if s[-1] == std:
                    s.pop()
                    std += 1
                    q.appendleft(cur)
                else:
                    s.append(cur)
            else:
                s.append(cur)
    else:
        if s[-1] == std:
            s.pop()
            std += 1
        else:
            print("Sad")
            isPrint = False
            break

if isPrint:
    print("Nice")