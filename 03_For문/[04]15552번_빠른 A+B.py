#15552번: 빠른 A+B
# sys.stdin.readline() 개행문자가 같이 입력됨 제거해야한다.

import sys

num = int(sys.stdin.readline())

for i in range(1,num+1):
    print(sum(map(int,sys.stdin.readline().split())))
