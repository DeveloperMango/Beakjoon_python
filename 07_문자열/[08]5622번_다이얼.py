#5622번: 다이얼 
#참고: https://www.acmicpc.net/problem/5622

dia = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
str = input()
sec = 0
for i in str:
    for j in dia:
        if i in j:
            sec += dia.index(j)+3
print(sec)
