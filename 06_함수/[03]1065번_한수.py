#1065번: 한수
#https://www.acmicpc.net/problem/1065


import sys
num = int(sys.stdin.readline())
sNum = 0

def cal(n):
    if n<100:
        return 1
    else:
        nums = list(map(int,str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2] :
            return 1
    return 0

for i in range(1,num+1):
    sNum += cal(i)

print(sNum)
