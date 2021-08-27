#2609번: 최대공약수와 최소공배수
#https://www.acmicpc.net/problem/2609

import sys

a,b= map(int,sys.stdin.readline().split())
result = 1

if a%b==0 or b%a==0:
    print(a,b, sep="\n") if a<b else print(b,a,sep="\n")
    
else:
    result = b-a if a<b else a-b

24 18
    if(b%3==0):
        print(a*3)
    else:
        print(a*2)
    
