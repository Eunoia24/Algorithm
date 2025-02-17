import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
buffer = [0]
for i in nums:
    buffer.append(buffer[-1] + i)

for i in range(m):
    a, b = map(int, input().split())
    print(buffer[b]-buffer[a-1])