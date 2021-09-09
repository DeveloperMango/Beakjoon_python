#11866번: 요세푸스 문제 0
#https://www.acmicpc.net/problem/11866

import sys

cnt,num = map(int,sys.stdin.readline().split())
arr = [i for i in range(1,cnt+1)]
res = []
for i in range(cnt):
    for _ in range(num-1):
        tmp = arr[0]
        arr = arr[1::]
        arr.append(tmp)
        
    res.append(arr[0])
    arr = arr[1::]

print("<",end="")
print(*res,sep=", ",end="")
print(">")
