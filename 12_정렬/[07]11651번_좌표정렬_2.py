#11651번: 좌표 정렬하기 2
#https://www.acmicpc.net/problem/11651


import sys

n = int(sys.stdin.readline())
so = []

for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
    
so.sort(key=lambda x: (x[1], x[0]))

for i in so:
    print(i[0], i[1])


'''
cnt = int(sys.stdin.readline())
num=[]

for i in range(cnt):
    num.append(list(map(int,sys.stdin.readline().split())))

for i in range(cnt-1):
    for j in range(1,cnt-i):
        if num[j-1][1] >= num[j][1]:
            if num[j-1][1] == num[j][1]:
                 if num[j-1]< num[j]:
                     continue         
            num[j],num[j-1]= num[j-1],num[j]

for i,j in num:
    print(i,j)
'''

