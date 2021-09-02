#3036번: 링
#https://www.acmicpc.net/problem/3036

import sys

def GCD(a,b):
    return GCD(b%a,a) if b%a else a

cnt = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))


for i in range(1, cnt):
    if num[0]%num[i] == 0:
        print(num[0]//num[i],"/1",sep="")
    else:
        val = GCD(num[0],num[i])
        print(num[0]//val,"/",num[i]//val,sep="")
