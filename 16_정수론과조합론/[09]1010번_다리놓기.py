#1010번: 다리놓기
#https://www.acmicpc.net/problem/1010

import sys

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

a,b = map(int,sys.stdin.readline().split())
print(factorial(a))
