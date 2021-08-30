#2609번: 최대공약수와 최소공배수
#https://www.acmicpc.net/problem/2609

import sys

a,b= map(int,sys.stdin.readline().split())

def gcd(a,b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b);


if a%b==0 or b%a==0:
    print(a,b, sep="\n") if a<b else print(b,a,sep="\n")
    
else:
    result = gcd(a,b)
    print(result,end=" ")
    result = result * (a//result) * (b//result)
    print(result)




    
