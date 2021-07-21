#2839번: 설탕 배달
#https://www.acmicpc.net/problem/2839

num=int(input())
res=0
while True:
        if num%5==0:
                res += num//5
                print(res)
                break
        else:
                num-=3
                res+=1

        if num<-1:
                print("-1")
                break
