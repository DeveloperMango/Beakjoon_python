#2630번: 색종이 만들기
#https://www.acmicpc.net/problem/2630
import sys


def color(x,y,num):
    global b, w
    tmp_arr = arr[x][y]
    for i in range(x, x+num):
        for j in range(y, y+num):
            if tmp_arr != arr[i][j]:
                color(x,y,num//2)
                color(x,y+num//2,num//2)
                color(x+num//2,y,num//2)
                color(x+num//2,y+num//2,num//2)
                return

    if tmp_arr==0:
        w+=1
        return
    else:
        b+=1
        return
  


b = 0
w = 0
num = int(sys.stdin.readline())
arr = []
for i in range(num):
    arr.append(list(map(int,sys.stdin.readline().split())))

color(0,0,num)
print(w,b,sep='\n')
