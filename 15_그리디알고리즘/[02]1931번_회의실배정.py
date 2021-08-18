#1931번: 회의실 배정
#https://www.acmicpc.net/problem/1931


import sys

line = int(sys.stdin.readline())
num = []

for i in range(line):
    num.append(list(map(int,sys.stdin.readline().split())))   

num = sorted(num, key = lambda x: (x[1], x[0]))

last = 0
cnt = 0
for i, j in num:
    if i >= last:
        cnt += 1
        last = j
print(cnt)
