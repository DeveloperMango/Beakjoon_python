#2675번: 문자열반복


n = int(input())
    
for i in range(0,n):
    cnt,str1 = input().split()
    for i in str1:
        print(i*int(cnt),end="")    
    print("");


