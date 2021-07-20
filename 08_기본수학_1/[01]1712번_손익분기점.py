#1712번: 손익분기점
#문제참고: https://www.acmicpc.net/problem/1712
#공식참고: 이익 = (판매가격-변동비)*판매량 - 고정비
#손익분기점이 존재하지않는 경우는 B가 C랑 같거나 보다 클 경우이다

a,b,c = map(int,input().split())

if(b>c or b==c):
    cnt = -1
else:
    cnt = a//(c-b)+1
    
print(cnt)

