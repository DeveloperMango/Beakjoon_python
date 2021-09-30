#2630번: 색종이 만들기
#https://www.acmicpc.net/problem/2630

import sys

def quadtree(x,y,num):
    tmp_arr = arr[x][y]
    print(tmp_arr)
    for i in range(x, x+num):
        for j in range(y, y+num):
            if tmp_arr != arr[i][j]:
                ans.append("(")
                quadtree(x,y,num//2)
                quadtree(x,y+num//2,num//2)
                quadtree(x+num//2,y,num//2)
                quadtree(x+num//2,y+num//2,num//2)
                ans.append(")")
                return            
            
    ans.append(tmp_arr)

num = int(sys.stdin.readline())
arr = []
ans = []
for i in range(num):
    arr.append(list(map(int,input())))

quadtree(0,0,num)
print(*ans, sep="")
