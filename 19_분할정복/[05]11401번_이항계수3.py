#11401번: 이항계수3
# https://www.acmicpc.net/problem/11401
#페르마 소정리 참고 / https://cantcoding.tistory.com/27
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
def divide(a,b):
    if b==1:
        return a%p
    elif b%2==1:
        return divide((a**2)%p,b//2)*a%p
    else:
        return divide((a**2)%p,b//2)
p=1000000007
a=1
b=1
t=min(n-m,m)
for i in range(t):
    a=a*(n-i)%p
    b=b*(t-i)%p
print((a*divide(b,p-2))%p)