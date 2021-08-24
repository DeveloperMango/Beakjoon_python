#2565번: 전깃줄
#https://www.acmicpc.net/problem/2565


import sys

num = int(sys.stdin.readline())

numlist = list(map(int,sys.stdin.readline().split()))
rev_list = numlist[::-1]

dp = [1 for _ in range(num)]    #증가
dm = [1 for _ in range(num)]    #감소

