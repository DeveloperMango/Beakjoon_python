#1436번: 영화감독 숌
#https://www.acmicpc.net/problem/1436

cnt = int(input())

num = 666
ck = 1

while True:

    if ck == cnt:
        print(num)
        break
    
    num += 1

    if str(num).find("666") != -1:
        ck +=1




    
