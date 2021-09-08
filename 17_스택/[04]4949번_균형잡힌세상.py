#4949번: 균형잡힌세상.py
#https://www.acmicpc.net/problem/4949

import sys

while True:
    line = sys.stdin.readline().rstrip()
    arr = []
    flag = 0
    if line==".":
        break
    
    for i in line:
        if i == "(" or i =="[":
            arr.append(i)
            
        elif i == ")":
            if arr and arr[-1] == "(":
                arr.pop()
            else:
                flag = 1
                break
            
        elif i == "]":
            if arr and arr[-1] == "[":
                arr.pop()
            else:
                flag = 1
                break

    print("yes" if not arr and flag == 0 else "no")
  
