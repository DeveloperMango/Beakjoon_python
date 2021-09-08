#9012번: 괄호
#https://www.acmicpc.net/problem/9012

import sys
cnt = int(sys.stdin.readline())
res = []

for i in range(cnt):

    res.clear()
    flag = 0
    line = input()
   
    if len(line) % 2 !=0:
        print("NO")
        continue

    else:
        for i in line:
            if i == "(":
                res.append(i)
            else:
                try:
                    res.pop()
                except:
                    flag = 1
                    break

    if len(res) == 0 and flag == 0:
        print("YES")
    else:
        print("NO")
            

