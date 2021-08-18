#11047번: 동전 0
#https://www.acmicpc.net/problem/11047


import sys

cnt,num = map(int,sys.stdin.readline().split())
num_list = [int(sys.stdin.readline()) for _ in range(cnt)]

ck = 0
cnt-=1

while num > 0:

    if num < num_list[cnt]:
        cnt-=1
    else:
        ck += num // num_list[cnt]
        num -= num_list[cnt] * (num // num_list[cnt])
        
print(ck)
