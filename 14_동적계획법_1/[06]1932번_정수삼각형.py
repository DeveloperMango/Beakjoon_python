#1932번: 정수 삼각형
#https://www.acmicpc.net/problem/1932


line = int(input())
num = []
p=2

for i in range(line):
    num.append(list(map(int,input().split())))   

for i in range(1,line):
    for j in range(p):
        if j == 0:
            num[i][j] = num[i][j] + num[i - 1][j]
        elif i == j:
            num[i][j] = num[i][j] + num[i - 1][j - 1]
        else:
            num[i][j] = max(num[i - 1][j - 1], num[i - 1][j]) + num[i][j]
    p += 1
    
print(max(num[line - 1]))



