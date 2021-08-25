#1912번: 연속합
#https://www.acmicpc.net/problem/1912


import sys

num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(num)]
dp[0] = arr[0]

for i in range(1,num):
    dp[i] = max(arr[i],dp[i-1]+arr[i])
    
print(max(dp))
