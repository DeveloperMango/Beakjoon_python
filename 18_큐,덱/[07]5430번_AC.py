#5430: AC
#https://www.acmicpc.net/problem/5430

import sys
from collections import deque

cnt= int(sys.stdin.readline())

for i in range(cnt):
    func = sys.stdin.readline().rstrip()
    arr_size = int(sys.stdin.readline())
    queue = sys.stdin.readline().rstrip()[1:-1].split(",")
    arr = deque(queue)
    rev = 0
    flag = 0

    for i in func:
        if i == 'R':
            rev +=1
        elif i == 'D':
            if len(arr) < 1 or arr_size==0:
                flag = 1
                print("error")
                break 
                
            if rev%2==0:
                arr.popleft()
            else:
                arr.pop()

    if not flag:
        if rev%2 !=0:
            arr.reverse()
        print("[" + ",".join(arr) + "]")
