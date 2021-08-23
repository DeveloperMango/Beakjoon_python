#2156번: 포도주 시식
#https://www.acmicpc.net/problem/2156

import sys

cnt = int(sys.stdin.readline())

num_list = [int(input()) for _ in range(cnt)]
dp = [0 for _ in range(cnt)]


if cnt == 1:
    dp[0] = num_list[0]
    
elif cnt == 2:
    dp[0] = num_list[0]
    dp[1] = num_list[0]+num_list[1]

else:
    dp[0] = num_list[0]
    dp[1] = num_list[0]+num_list[1]
    dp[2] = max(dp[1],num_list[2]+num_list[0],num_list[2]+num_list[1])

for i in range(3,cnt):
    dp[i] = max(max(num_list[i] + num_list[i-1] + dp[i-3],num_list[i]+dp[i-2]),dp[i-1])

print(dp[cnt-1])
