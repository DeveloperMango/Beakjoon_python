#2981번: 검문 
#https://www.acmicpc.net/problem/2981

import sys

def GCD(a,b):
    return GCD(b%a,a) if b%a else a

ans = list()
cnt = int(sys.stdin.readline())
num = list(int(sys.stdin.readline()) for _ in range(cnt))
gcdval = abs(num[1]-num[0])

for i in range(2, cnt):
    gcdval = GCD(gcdval,abs(num[i] - num[i-1]))

for i in range(2,int(gcdval**0.5)+1):
    if gcdval % i == 0:
        ans.append(i)
        ans.append(gcdval//i)

ans.append(gcdval)
ans = list(set(ans))
ans.sort()
print(*ans)
