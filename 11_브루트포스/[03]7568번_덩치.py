#7568번: 덩치
#https://www.acmicpc.net/problem/7568

cnt = int(input())

x = [0 for i in range(cnt)]
y = [0 for i in range(cnt)]

for i in range(cnt):
   x[i],y[i] = map(int,input().split())

for i in range(cnt):
    rank = 1
    for j in range(cnt):
        if i !=j:
            if x[i]<x[j] and y[i]<y[j]:
                rank+=1

    print(rank, end=" ")
