import sys

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

tree, interval = [], []
for i in range(int(input())):
    tree.append(int(input()))
    if i > 0:
        interval.append(tree[-1] - tree[-2])

answer = gcd(interval[0], interval[1])
for i in range(2, len(interval)):
        answer = gcd(answer, interval[i])

print((tree[-1] - tree[0]) // answer - len(tree) + 1)