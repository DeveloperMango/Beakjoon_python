
#3009번: 네 번째 점
#https://www.acmicpc.net/problem/3009

#a,b = [list(map(int, input().split())) for _ in range(3)]


    
x,y=[],[]
for _ in range(3):
    a,b=map(int,input().split())

    if a in x:
        x.remove(a)
    else:
        x.append(a)

    if b in y:
        y.remove(b)
    else:
        y.append(b)
        
print(x,y)
