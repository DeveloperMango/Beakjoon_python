#10872번: 팩토리얼
#https://www.acmicpc.net/problem/10872


def fac(num):
    if num > 1:
        return num * fac(num-1)
    else :
        return 1 #ex)2^0=1
    
print(fac(int(input())))
