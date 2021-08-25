#1149번: RGB거리
#https://www.acmicpc.net/problem/1149

import sys

cnt = int(sys.stdin.readline())

arr = []
for i in range(cnt):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(1, cnt):
    arr[i][0] = min(arr[i-1][1],arr[i-1][2])+arr[i][0]
    arr[i][1] = min(arr[i-1][0],arr[i-1][2])+arr[i][1]
    arr[i][2] = min(arr[i-1][0],arr[i-1][1])+arr[i][2]

print(min(arr[cnt-1]))
