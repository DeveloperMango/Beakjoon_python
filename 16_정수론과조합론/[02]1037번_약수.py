#1037번: 약수
#https://www.acmicpc.net/problem/1037

import sys

cnt = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

print(min(num)*max(num))
