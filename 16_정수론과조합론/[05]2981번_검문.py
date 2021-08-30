#1934번: 최소공배수
#https://www.acmicpc.net/problem/1934

import sys
cnt = int(sys.stdin.readline())



def LCM(a,b):
    tmp = GCD(a,b)
    return int((a*b)/tmp)


def GCD(a,b):
    return GCD(b%a,a) if b%a else a


for i in range(cnt):
    a,b= map(int,sys.stdin.readline().split())
    print(LCM(a,b))




    
