#1330번: 두 수 비교하기

a,b=map(int,input().split())
print('>') if a>b else print('<') if a<b else print('==') 

#print(['><'[a<b],'=='][a==b]) 숏코딩
