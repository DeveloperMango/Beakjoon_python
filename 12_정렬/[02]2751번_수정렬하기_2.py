#2751번: 수 정렬하기 2
#https://www.acmicpc.net/problem/2751

import sys

cnt = int(sys.stdin.readline())

arr = []
for i in range(cnt):
    arr.append(int(sys.stdin.readline()))

def merge_sort(arr):
    if len(arr) < 2:
        return arr
        
    mid = len(arr)//2
    right = merge_sort(arr[:mid])
    left = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(right) and h < len(left):
        if right[l] < left[h]:
            merged_arr.append(right[l])
            l += 1
        else:
            merged_arr.append(left[h])
            h += 1
            
    merged_arr += right[l:]
    merged_arr += left[h:]
    return merged_arr


arr = merge_sort(arr)
for i in arr:
    print(i)
