#1676번: 팩토리얼 0의 개수
#https://www.acmicpc.net/problem/1676
import sys

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

a = int(sys.stdin.readline())
num = factorial(a)

res = 0
while True:    
    if num % 10 == 0:
        num //= 10
        res+=1
    else:
        break
    
print(res)
