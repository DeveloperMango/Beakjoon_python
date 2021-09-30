#11053번: 가장 긴 증가하는 부분 수열
#https://www.acmicpc.net/problem/11053


import sys

num = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))

dp = [0 for i in range(num)]

for i in range(num):
    for j in range(i):
        if numlist[i] > numlist[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    print(dp)
    
print(max(dp))
