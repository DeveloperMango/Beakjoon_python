
#1929번: 소수
#https://www.acmicpc.net/problem/1929

'''
에라토스테네스의 체
대표적인 소수 판별 알고리즘으로 빠르고 정확하게 구하는 방법
'''


a,b= map(int,input().split())
ran=[i for i in range(a,b+1)]

for i in ran:
    if(i==1): continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            i=0
            break
    if i!=0: print(i)
