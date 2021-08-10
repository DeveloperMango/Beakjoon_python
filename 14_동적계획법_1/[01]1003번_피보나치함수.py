#1003번: 피보나치 함수
#https://www.acmicpc.net/problem/1003
 
zero = [1,0,1]
one = [0,1,1]
 
def cal(num):
    i_len = len(zero)
    
    if i_len <= num:
        for i in range(i_len,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
            
    print(zero[num],one[num])

num = int(input())

for i in range(num):
    k = int(input())
    cal(k)
