#18870번: 좌표압축
#https://www.acmicpc.net/problem/18870

import sys

cnt = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))

result = sorted(list(set(num)))

#딕셔너리(dictionary) : 값(value)에게 이름(key)을 붙여서 매칭
dic = {result[i] : i for i in range(len(result))}

for i in num:
    print(dic[i], end = ' ')

    


