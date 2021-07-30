#2798번: 블랙잭
#https://www.acmicpc.net/problem/2798


cnt,m = map(int,input().split())
arr = list(map(int,input().split()))
tmp = 0

for i in range(cnt):
    for j in range(cnt):
        if i!=j:
            for k in range(cnt):
                if i!=k and j!=k:
                    p = arr[i] + arr[j] + arr[k]
                    if tmp< p and p<=m:
                        tmp = p
print(tmp)
