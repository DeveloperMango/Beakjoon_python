#11933번: ATM
#https://www.acmicpc.net/problem/11399


import sys

cnt = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

for i in range(1,cnt):
    arr[i] += arr[i-1]
    
print(sum(arr))
