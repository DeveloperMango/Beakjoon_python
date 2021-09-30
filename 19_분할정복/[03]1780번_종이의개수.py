#1780번: 종이의 개수
#https://www.acmicpc.net/problem/1780

import sys

num = int(sys.stdin.readline())
arr = []
ans_list = [0,0,0]

for i in range(num):
    arr.append(list(map(int,sys.stdin.readline().split())))

def papertree(x,y,num):
    tmp_arr = arr[x][y]
    rtn = [0, 0, 0]
    for i in range(num):
        for j in range(num):
            if tmp_arr != arr[x+i][y+j]:
                rtn = divide(x, y, num)
                return rtn
            
    rtn[tmp_arr+1] += 1
    return rtn

def divide(x, y, num):
    result = [0, 0, 0]
    temp = []
    for i in range(3):
        for j in range(3):
            temp = papertree(x + i* num//3, y + j* num//3, num//3)
            result[0] += temp[0]
            result[1] += temp[1]
            result[2] += temp[2]
    return result


ans_list = papertree(0,0,num)
print(*ans_list,sep='\n')
