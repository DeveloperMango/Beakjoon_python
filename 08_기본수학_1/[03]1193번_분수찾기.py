#1193번: 분수찾기
#문제참고: https://www.acmicpc.net/problem/1193

'''
0,0 -,+

0,1 +,-
1,0 +,-

2,0 -,+
1,1 -,+
0,2 -,+

0,3 +,-
1,2 +,-
2,1 +,-
3,0 +,-
'''

num = int(input())
i=0
j=0
k=1
cnt = 1

while True:
    if cnt==num:
        print(i+1,"/",j+1 ,sep="")
        break
    else: k+=1
        
    for _ in range(k):
        if k%2==0:
            i+=1
            if(j!=0):j-=1
        elif k%2==1:
            j+=1
            if(i!=0):   i-=1       
        cnt+=1
        if cnt==num:    break  
   



