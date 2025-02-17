prime, check = [], [0] * 1000001
check[0], check[1] = 1, 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

for i in range(int(input())):
    cnt = 0
    n = int(input())
    for j in prime:
        if j >= n:
            break
        if not check[n - j] and j  <= n - j:
            cnt += 1
    print(cnt)