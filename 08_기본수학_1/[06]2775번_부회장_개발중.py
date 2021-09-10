#2775번: 부회장이 될테야
#https://www.acmicpc.net/problem/2775

import sys
cnt = int(sys.stdin.readline())

for i in range(cnt):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())
    res = 0
    
    for i in range(floor):
        for j in range(1,room+1):
            if i == 0:
                res += j
            else:
                
