#13305번: 주유소
#https://www.acmicpc.net/problem/13305

import sys

cnt = int(sys.stdin.readline())
len_arr = list(map(int,sys.stdin.readline().split()))
fee_arr = list(map(int,sys.stdin.readline().split()))

temp = fee_arr[0]

result = len_arr[0] * temp

for i in range(1, len(len_arr)):
    if fee_arr[i] < temp:
        result += len_arr[i] * fee_arr[i]
        temp = fee_arr[i]
    else:
        result += len_arr[i] * temp

print(result)



''' 17점
for i in range(len(len_arr)):
    if fee_arr[i] != min(fee_arr[:len(fee_arr)-1]):
        fee_arr[i] = fee_arr[i]*len_arr[i]
    else: 
        fee_arr[i] = fee_arr[i]*sum(len_arr[i:len(len_arr)])
        print(sum(fee_arr[:i+1]))
        break
'''
