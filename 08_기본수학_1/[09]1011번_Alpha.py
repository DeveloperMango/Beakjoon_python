#1011번: Fly me to the Alpha Centauri
#https://www.acmicpc.net/problem/1011


'''
1 = 1
2 = 1 1
3 = 1 1 1
4 = 1 2 1

5 = 1 2 1 1
6 = 1 2 2 1
7 = 1 2 2 1 1
8 = 1 2 2 2 1

9 = 1 2 3 2 1
10 = 1 2 3 2 1 1
'''


import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
    a,b = map(int,sys.stdin.readline().split())
    diff = b-a
    num = 1
    
    while True:
        #3까지의 범위를 찾는 과정
        if num ** 2 <= diff < (num + 1) ** 2:
            break
        num += 1
        
    if num ** 2 ==  diff:
        print((num * 2) - 1)
    elif num ** 2 < diff <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)
        

        
            
