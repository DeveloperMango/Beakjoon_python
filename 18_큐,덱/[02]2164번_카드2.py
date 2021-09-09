#2164번: 카드2
#https://www.acmicpc.net/problem/2164

import sys
from collections import deque

cnt = int(sys.stdin.readline())
arr = [i for i in range(1,cnt+1)]

while len(arr) > 1:
    if len(arr) % 2 != 0:
        t = [arr[-1]]
        t.extend(arr[1::2])
        arr = t
    else:
        arr = arr[1::2]
        
print(arr[0])


