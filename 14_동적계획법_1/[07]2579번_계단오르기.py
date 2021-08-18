#1932번: 정수 삼각형
#https://www.acmicpc.net/problem/1932

import sys 

line =  int(sys.stdin.readline())
dp = []
arr = []
for _ in range(line):
        arr.append(int(sys.stdin.readline()))

if line == 1:
        dp.append(arr[0])
elif line == 2:
        dp.append(arr[0])
        dp.append(arr[0]+arr[1])
elif line == 3:
        dp.append(arr[0])
        dp.append(arr[0]+arr[1])
        dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
else:
        dp.append(arr[0])
        dp.append(arr[0]+arr[1])
        dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))

        for i in range(3,line): #전칸,전전칸 올라온 경우 최댓값
                dp.append(max(dp[i-3] + arr[i] + arr[i-1], dp[i-2] + arr[i]))	


print(dp.pop())

