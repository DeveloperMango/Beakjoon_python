#2562번: 최댓값

#print(num.index(maxnum))
#index 위치 반환



num=[]
for i in range(0,9):
    num.append(int(input()))

maxnum = max(num)
print(maxnum)
print(num.index(maxnum)+1)



