#2565번: 전깃줄
#https://www.acmicpc.net/problem/2565


import sys

num = int(sys.stdin.readline())
numlist = []

for i in range(num):
    numlist.append(list(map(int,sys.stdin.readline().split())))



numlist.sort()
print(numlist)

dp = [1]*num
for i in range(num):
    for j in range(i):
        print(i, j ,numlist[i][1],numlist[j][1], dp)
        
        if numlist[i][1] > numlist[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(num-max(dp))
