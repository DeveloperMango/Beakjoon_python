#2231번: 분해합
#https://www.acmicpc.net/problem/2231

# 216 198
num = int(input())

for i in range(num):
    tmp = i
    i_sum = 0

    while tmp!=0:
        i_sum += tmp%10
        tmp=tmp//10

    if i_sum+i == num:
        print(i)
        exit()
        
print("0")
