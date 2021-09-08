#18258번: 큐2
#https://www.acmicpc.net/problem/18258

import sys
from collections import deque

cnt = int(sys.stdin.readline())
arr = [i for i in range(1,cnt+1)]

while len(arr) > 1:
    if len(arr) % 2:
        ans = [arr[-1]]
        t.append(arr[1::2])
        arr = t
        
    else:
        arr = arr[1::2]

print(*arr[0])

