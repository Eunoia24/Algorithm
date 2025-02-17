L,cnt = [], 0
def hanoi(n, s=1, d=3, t=2):
    global L, cnt
    if n == 1:
        L.append([s, d])
        cnt += 1
    else:
        hanoi(n-1, s, t, d)
        L.append([s, d])
        cnt += 1
        hanoi(n-1, t, d, s)

hanoi(int(input()))
print(cnt)
for i in L:
    print(i[0], i[1])