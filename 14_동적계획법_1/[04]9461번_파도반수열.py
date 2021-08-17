#9461번: 파도반 수열
#https://www.acmicpc.net/problem/9461

import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
    p = [1,1,1,2,2]
    num = int(sys.stdin.readline())

    for k in range(5,num+1):
        p.append(p[k-1]+p[k-5])
  
    print(p[num-1])
