#2908번: 상수
#참고: https://www.acmicpc.net/problem/2908


a,b=map(str,input().split())

a = ''.join(reversed(a))
b = ''.join(reversed(b))

if int(a)<int(b):   print(b)
else:   print(a)


#print(max(input()[::-1].split()))
