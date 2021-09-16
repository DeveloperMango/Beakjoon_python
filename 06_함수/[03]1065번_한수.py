#1065번: 한수
#https://www.acmicpc.net/problem/1065

'''
문제해석
한수의 뜻은 " 각 자리수들이 등차수열을 이루는 수" 이다. 
이때 등차수열이란 각 항들이 일정한 차이를 보이는 수열이다
예를들어 한수는 123(공차1), 753(공차-2)가능하다. 공차먹고싶다.
여기서 중요한점은 1,2자리수들은 모두 한수로 취급된다.
1자리인 경우는 비교할 수들이 없어 한수로 인정된다.
2자리인 경우는 공차가 한개밖에 되지 않아서 한수로 인정된다.
'''

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
