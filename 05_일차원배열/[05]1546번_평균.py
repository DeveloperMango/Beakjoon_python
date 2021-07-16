#1546번: 평균

cnt = int(input())
score = list(map(int,input().split()))
maxnum = int(max(score))

avg = 0.0
newScore = []
for i in score:
    newScore.append(i/maxnum*100)
  
avg = sum(newScore,0.0)/cnt
print(avg)
