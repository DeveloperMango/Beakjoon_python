#10250번: ACM호텔
#https://www.acmicpc.net/problem/10250


#6 12 10
#30 50 72  1203
#6 12 12

num = int(input())

for i in range(num):
    h,w,cnt = map(int,input().split())
    i = cnt//h+1
    j = cnt%h

    if cnt%h ==0:
        i = cnt//h
        j = h        
    print(j*100+i)
