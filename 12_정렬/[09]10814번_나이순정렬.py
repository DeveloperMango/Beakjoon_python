#10814번: 나이순정렬
#https://www.acmicpc.net/problem/10814

import sys

cnt = int(sys.stdin.readline())

words_list = []

for _ in range(cnt):
    words_list.append(list(sys.stdin.readline().split()))

words_list.sort(key = lambda a: int(a[0]))

for i,j in words_list:
    print(i,j)



