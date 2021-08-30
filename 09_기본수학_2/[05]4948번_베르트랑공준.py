#4948번: 베르트랑 공준
#https://www.acmicpc.net/problem/4948
#소수찾기 -> 에라토스테네스의 체

def prime_list(n):
    nums = [0, 0] + [1] * (2*n-1)
    
    for i in range(2, int((2*n)**0.5)+1):
        if nums[i] == 1:
            nums[2*i::i] = [0] * ((2*n-i)//i)
    return nums[n+1:].count(1)

while True:
    n = int(input())
    
    if n == 0:
        break
    else:
        print(prime_list(n))
