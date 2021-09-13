#10757번: 큰 수 A+B
#https://www.acmicpc.net/problem/10757

import sys

a,b = list(map(str,sys.stdin.readline().split()))

print(a,b)

a.reverse()
b.reverse()


cnt = len(a) if len(a) > len(b) else len(b)
carry = 0
res=[]
for i in range(cnt):
    sum = a[i] + b[i] + carry

    if sum > 9:
        carry = 1
    else:
        carry = 0

    res[i] = sum%10
