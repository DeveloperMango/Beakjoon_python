#1193번: 분수찾기
#문제참고: https://www.acmicpc.net/problem/1193

'''
문제해석
분수의 일정한 규칙이 존재한다.
 i번째 대각선에서는 i까지 분자가 증가합니다.
분자는 홀수번째 대각선에서 아래로 증가, 짝수번째 대각선에서 위로 증가하고 있습니다.
분모는 분자의 반대 방향으로 이루어져 있어서,
분자를 구한 후, i+1에서 분자를 뺀 값을 분모로 사용할 수 있습니다.
'''

x = int(input())
num_list = []

num = 0
num_count = 0

while num_count < x:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = x - num_count
    j = num - i + 1
else:
    i = num - (x - num_count) + 1
    j = x - num_count

print(f"{i}/{j}")



