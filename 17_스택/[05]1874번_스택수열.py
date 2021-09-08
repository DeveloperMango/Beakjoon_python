#1874번: 스택수열.py
#https://www.acmicpc.net/problem/1874

import sys
cnt = int(sys.stdin.readline())

res = []
arr = []
ck = 1

for val in range(1,cnt+1):
    
    num = int(sys.stdin.readline())

    if not res or num != res[-1]:
        for i in range(ck,num+1):
            res.append(i)
            arr.append("+")
        ck = num+1
        
    if res[-1] > num:
        break
    else:
        num == res[-1]
        res.pop()
        arr.append("-")

print(*arr,sep="\n") if(len(res) == 0) else print("NO")
    


