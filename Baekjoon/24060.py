import math, sys
input = sys.stdin.readline
cnt = 0

def merge_sort(arr):
    global cnt, K
    if len(arr) < 2:
        return arr

    mid = math.ceil(len(arr) / 2)
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    
    if K > len(merged_arr):
        K -= len(merged_arr)
    else:
        print(merged_arr[K - 1])
        exit()
        
    return merged_arr


A, K = map(int, input().split())
arr = list(map(int, input().split()))
merge_sort(arr)
print(-1)