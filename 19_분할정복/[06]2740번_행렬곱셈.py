#2740번: 행렬 곱셈
#https://www.acmicpc.net/problem/2740

import sys

def DaC(a,b):
    if b==1:
        return a%c

    temp = DaC(a,b//2)

    if b%2==0:
        return temp*temp%c
    else:
        return temp*temp*a%c
	
a,b,c = map(int,sys.stdin.readline().split())
print(DaC(a,b))

