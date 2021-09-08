#1874번: 스택수열.py
#https://www.acmicpc.net/problem/1874
'''
import sys
cnt = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
stack = []
res = [-1 for _ in range(cnt)]

for i in range(cnt):    
    for j in range(i,cnt):
        if arr[i] < arr[j]:
            res[i] = arr[j]
            break
        
print(*res)
'''

import sys

cnt = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
stack = []
res = [-1 for _ in range(cnt)]

for i in range(cnt):
    try:
        while arr[stack[-1]]<arr[i]:
            res[stack.pop()] = arr[i]
    except:
        pass

    stack.append(i)

print(*res)
