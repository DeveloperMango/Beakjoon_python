#10866번: 
#https://www.acmicpc.net/problem/10866

import sys

cnt = int(sys.stdin.readline())
arr = []

for _ in range(cnt):
    line = sys.stdin.readline()

    if "push_front" in line:
        tmp = [line.split()[1]]
        tmp.extend(arr)
        arr = tmp
        
    elif "push_back" in line:
        arr.append(line.split()[1])

    elif "pop_front" in line:
         print("-1") if not arr else print(arr[0])
         arr= arr[1::]
   
    elif "pop_back" in line:
        print("-1") if not arr else print(arr.pop())
        
    elif "size" in line:
        print(len(arr))
        
    elif "empty" in line:
        print("1") if not arr else print("0")
        
    elif "front" in line:
        print("-1")  if not arr else print(arr[0])
        
    elif "back" in line:
        print("-1")  if not arr else print(arr[-1])
