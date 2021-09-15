#10757번: 큰 수 A+B
#https://www.acmicpc.net/problem/10757

import sys

a,b = sys.stdin.readline().split()

if len(a) < len(b):
    a,b=b,a
    
carry = 0
res=[]

b= '0'*(len(a)-len(b))+b

for i in range(len(a)-1,-1,-1):
    sum = int(a[i]) + int(b[i]) + carry
    
    if sum > 9:
        carry = 1
    else:
        carry = 0

    res.append(sum%10)

if carry:
    res.append(str(1))
    
print(*res[::-1],sep="")
