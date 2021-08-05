#1427번: 소트인사이드
#https://www.acmicpc.net/problem/1427


arr = list(input())

for i in range(len(arr)):
    for j in range(i,len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
        print(arr)
