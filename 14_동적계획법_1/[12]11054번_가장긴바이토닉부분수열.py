#11054번: 가장 긴 바이토닉 부분 수열
#https://www.acmicpc.net/problem/11053


import sys

num = int(sys.stdin.readline())

numlist = list(map(int,sys.stdin.readline().split()))
rev_list = numlist[::-1]

dp = [1 for _ in range(num)]    #증가
dm = [1 for _ in range(num)]    #감소

for i in range(num):
    for j in range(i):
        if numlist[i] > numlist[j]:
            dp[i] = max(dp[i],dp[j]+1)

        if rev_list[i]>rev_list[j]:
            dm[i] = max(dm[i],dm[j]+1)

result = [0 for i in range(num)]
for i in range(num):
    result[i] = dp[i] + dm[num-i-1]-1

print(max(result))
