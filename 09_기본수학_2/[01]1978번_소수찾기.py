#1978번: 소수찾기
#https://www.acmicpc.net/problem/1978

N = int(input())
n = list(map(int, input().split()))
result = 0

for i in n:
    sosu = 0
    
    if i>1:
        for j in range(2, i+1):
            if i%j == 0:
                sosu += 1
    if sosu==1:
        result += 1

print(result)
