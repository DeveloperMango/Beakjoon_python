#10430번: 나머지

A,B,C = map(int,input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C , sep="\n")

#숏코딩:print(x:=(a+b)%c,x,y:=a*b%c,y)

# := (바다코끼리 연산자)
# 표현식(Expression)에 이름을 부여하고 재사용할 수 있게 하는 것
