import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))
op = ['+' for _ in range(op_cnt[0])] + \
     ['-' for _ in range(op_cnt[1])] + \
     ['*' for _ in range(op_cnt[2])] + \
     ['/' for _ in range(op_cnt[3])] # int()로 나눗셈 진행

signs = list(permutations(op, len(op)))

maximum, minimum = -1e9, 1e9
for i in signs:
    tmp = nums[0]
    for idx, j in enumerate(i):
        if idx == 0: continue
        if j == '+': tmp += nums[idx]
        elif j == '-': tmp -= nums[idx]
        elif j == '*': tmp *= nums[idx]
        else: tmp = int(tmp / nums[idx])
    if tmp > maximum: maximum = tmp
    if tmp < minimum: minimum = tmp

print(f"{maximum}\n{minimum}")