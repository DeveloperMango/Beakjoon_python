#10872번: 피보나치수 5
#https://www.acmicpc.net/problem/10872


def fibo(num):
    if num>=2:
        return fibo(num-1)+fibo(num-2)
    else:
        return num

print(fibo(int(input())))
