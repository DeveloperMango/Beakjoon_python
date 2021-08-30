#2750번: 수 정렬하기
#https://www.acmicpc.net/problem/2750

cnt = int(input())
arr = []
for i in range(cnt):
    arr.append(int(input()))

for i in range(cnt):
    for j in range(cnt):
        if arr[i]<arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

for n in arr:
    print(n)
             
