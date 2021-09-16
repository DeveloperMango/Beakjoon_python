#10250번: ACM호텔
#https://www.acmicpc.net/problem/10250


num = int(input())

for i in range(num):
    h,w,cnt = map(int,input().split())
    i = cnt//h+1
    j = cnt%h

    #꼭대기 층인 경우
    if cnt%h ==0:
        i = cnt//h
        j = h  
      
    print(j*100+i)