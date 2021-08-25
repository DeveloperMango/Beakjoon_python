#9251번: LCS
#https://www.acmicpc.net/problem/9251


arr1 = list(input())
arr2 = list(input())

len1 = len(arr1)
len2 = len(arr2)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
print(dp[-1][-1])
