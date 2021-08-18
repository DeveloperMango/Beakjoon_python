#11651번: 좌표 정렬하기 2
#https://www.acmicpc.net/problem/11651

cnt = int(input())
num=[]

for i in range(cnt):
    num.append(list(map(int,input().split())))

for i in range(num):
    for j in range(num-1):
        if num[i][j]>=num[i][j+1]:
            
print(num)
