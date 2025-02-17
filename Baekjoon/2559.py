n, k = map(int, input().split())
temp = list(map(int, input().split()))
tmp = sum(temp[:k])
result = [tmp]
for i in range(k, len(temp)):
    tmp = tmp - temp[i-k] + temp[i]
    result.append(tmp)

print(max(result))