#10809번: 알파벳 찾기

s = input()

list = [-1 for _ in range(26)]

for i in s:
    list[ord(i)%97] = s.index(i)

for i in list:
    print(i, end=" ")

