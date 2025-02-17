import sys
lst = [int(input())]

def bfs(depth=0):
    global lst
    if 1 in lst:
        print(depth)
        return
    else:
        temp = []
        while lst:
            cur = lst.pop()
            if cur % 3 == 0:
                temp.append(cur // 3)
            if cur % 2 == 0:
                temp.append(cur // 2)
            temp.append(cur - 1)
        lst = temp[:]
        bfs(depth + 1)

bfs()