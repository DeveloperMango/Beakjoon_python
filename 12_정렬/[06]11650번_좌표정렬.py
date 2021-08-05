#11650번: 좌표정렬
#https://www.acmicpc.net/problem/11650

#lambda를 사용하여 정렬 기준을 정함
# 첫번째 인자(x[0]) x 정렬, 두번째인자(x[1]) y 정렬


import sys
    
cnt = int(sys.stdin.readline())
xy=[]

for i in range(cnt):
    x,y=map(int,sys.stdin.readline().split())
    xy.append((x,y))

xy.sort(key=lambda x:(x[0],x[1]))

for i in range(cnt):
    print(xy[i][0],xy[i][1])
