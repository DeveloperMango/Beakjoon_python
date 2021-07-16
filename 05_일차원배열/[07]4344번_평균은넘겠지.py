# 4344번: 평균은 넘겠지

cnt = int(input())

for i in range(0,cnt):
    
    score = list(map(int,input().split()))
    avg = sum(score[1:])/score[0]   #SUM범위지정
    ck = 0
    
    for j in range(1,score[0]+1):
        if avg<score[j]:
            ck += 1

    rate = (ck/score[0])*100
    
    print("%0.3f"%rate,"%" , sep="")
    #print("{0:.3f%}".rate)
