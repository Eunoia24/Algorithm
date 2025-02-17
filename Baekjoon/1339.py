words = []
for _ in range(int(input())):
    words.append(input())

alpha = dict()
for i in words:
    for idx, j in enumerate(i):
        try:
            alpha[j] += 10 ** (len(i)-idx-1)
        except:
            alpha[j] = 10 ** (len(i)-idx-1)

values = sorted(list(alpha.values()), reverse=True)
result = 0
for i in range(9, 9 - len(values), -1):
    result += i * values[9 - i]

print(result)