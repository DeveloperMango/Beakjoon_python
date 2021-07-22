
#9020번: 골드바흐의추측
#https://www.acmicpc.net/problem/9020



cnt = int(input())

def CkPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(cnt):
    num = int(input())
    for j in range(num//2,1,-1):
        if CkPrime(num-j) and CkPrime(j):
            print(j,num-j)
            break




