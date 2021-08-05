#2108번: 통계학
#https://www.acmicpc.net/problem/2108

#Counter: 요소의 갯수
#most_common: 빈도수가 높은 순으로 출력

import sys
from collections import Counter

def mode(arr):
    c_arr = Counter(arr).most_common()
    
    if len(arr) > 1:
        if c_arr[0][1] == c_arr[1][1]:
            print(c_arr[1][0])
        else:
            print(c_arr[0][0])
    else:
        print(c_arr[0][0])
    

cnt = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(cnt)]
arr = sorted(arr)

print(round(sum(arr)/cnt))
print(arr[len(arr)//2])
mode(arr)
print(arr[cnt-1]-arr[0])
