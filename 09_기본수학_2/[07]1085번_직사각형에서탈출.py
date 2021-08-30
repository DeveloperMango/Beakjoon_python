#1085번: 직사각형에서 탈출
#https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

#x-0, y-0
distance = [x, y, w-x, h-y]
print(min(distance))
