#10828번: 스택
#https://www.acmicpc.net/problem/10828

import sys
cnt = int(sys.stdin.readline())
arr=[]

for i in range(cnt):
    ans = sys.stdin.readline()

    if "push" in ans:
        arr.append(ans.split()[1])
        
    elif "top" in ans:
        print("-1")  if not arr else  print(arr[len(arr)-1])
        
    elif "size" in ans:
        print(len(arr))
        
    elif "empty" in ans:
        print("1") if not arr else print("0")
        
    elif "pop" in ans:
       print("-1")  if not arr else print(arr.pop())
    


