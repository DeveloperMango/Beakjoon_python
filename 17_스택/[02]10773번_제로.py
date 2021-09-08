#10773번: 제로
#https://www.acmicpc.net/problem/10773

import sys
cnt = int(sys.stdin.readline())
arr=[]

for i in range(cnt):
    ans = int(sys.stdin.readline())
    
    if not ans:
        arr.pop()
    else:
        arr.append(ans)
       
print(sum(arr))
