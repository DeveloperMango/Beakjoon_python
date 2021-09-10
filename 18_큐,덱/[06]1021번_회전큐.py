#1021번: 회전큐
#https://www.acmicpc.net/problem/1021

import sys

cnt, num_cnt = map(int,sys.stdin.readline().split())
num_arr = list(map(int,sys.stdin.readline().split()))
cnt_arr = [i for i in range(1, cnt+1)]
res=[0 for _ in range(3)]

for i in range(num_cnt):
    for j in range(cnt):
        if num_arr[i] == cnt_arr[0]:
            cnt_arr = cnt_arr[1::]
            break

        else:
            if len(cnt_arr)//2 >= cnt_arr.index(num_arr[i]):
                tmp = cnt_arr[0]
                cnt_arr = cnt_arr[1::]
                cnt_arr.append(tmp)
                res[1]+=1
                
            elif len(cnt_arr)//2 < cnt_arr.index(num_arr[i]):
                tmp = [cnt_arr[-1]]
                cnt_arr.pop()
                tmp.extend(cnt_arr)
                cnt_arr = tmp
                res[2]+=1
        
print(max(res[0],res[1]+res[2]))
