import sys

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right, sum = 0, 0, 0
min_length = sys.maxsize

while True:
    if sum >= S:
        min_length = min(right - left, min_length)
        sum -= nums[left]
        left += 1
    elif right == N:
        break
    else:
        sum += nums[right]
        right += 1

print(0) if min_length == sys.maxsize else print(min_length)