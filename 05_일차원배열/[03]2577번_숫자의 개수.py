#2577번: 숫자의 개수

cal = [int(input()) for i in range(0,3)]
res = cal[0]*cal[1]*cal[2]

n_list = list(map(int,str(res)))
num = [0,0,0,0,0,0,0,0,0,0]

for i in n_list:
    num[i]+=1

for i in num:
    print(i)

