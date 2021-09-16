#2581번: 소수
#https://www.acmicpc.net/problem/2581

a = int(input())
b = int(input())
res=[]

for i in range(a,b+1):
    for j in range(2,i+1):     
        if i%j==0 and i!=j:
            break
        if i==j:
            res.append(i)

if not res:
    print("-1")
else:
    print(sum(res),res[0],sep='\n')