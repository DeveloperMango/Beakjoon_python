#2869번: 달팽이는 올라가고 싶다.
#문제참고: https://www.acmicpc.net/problem/2869
#반복문을 사용하면 시간초과발생 -> 등차수열공식을 이용하여 해결

import math
a,b,c = map(int,input().split())
print(math.ceil((c-a)/(a-b)+1))
