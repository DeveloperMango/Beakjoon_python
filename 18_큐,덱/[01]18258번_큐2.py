#18258번: 큐2
#https://www.acmicpc.net/problem/18258

import sys
from collections import deque

cnt = int(sys.stdin.readline())
arr = deque([])

for _ in range(cnt):
    line = sys.stdin.readline()

    if "push" in line:
        arr.append(line.split()[1])
        
    elif "pop" in line:
        print("-1") if not arr else print(arr.popleft())
        
    elif "size" in line:
        print(len(arr))
        
    elif "empty" in line:
        print("1") if not arr else print("0")
        
    elif "front" in line:
        print("-1")  if not arr else print(arr[0])
        
    elif "back" in line:
        print("-1")  if not arr else print(arr[-1])
